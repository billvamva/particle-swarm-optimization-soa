    def chaotic_search(self, x, pbest, pbest_value, gbest, gbest_cost, gbest_cost_history, curr_iter):
        '''
        This method performs chaotic search for C times in case premature convergence is detected

        Args:
        - Particle Positions
        - Global Best Position
        - Global Best Value
        - Current Iteration

        Returns:
        -
        '''
        
        p = 1 - (1 / 1 + np.log(curr_iter))
        
        def tent_map_1(x):
            if p > random.uniform(0, 1):
                return 2 * x
            else: 
                return x
        
        def tent_map_2(x):
            if p > random.uniform(0,1):
                return 2 * (1 - x)
            else:
                return x

        p = np.copy(gbest)

        # Chaotic Search Using Tent Mapping
        for i in range(0, self.c):

            print(f'{i}/{self.c}')

            # Map to interval [0, 1]
            z = np.interp(p, [self.min_val, self.max_val], [0, 1])
            
            # Tent Mapping
            conds = [z < 0.5, z >= 0.5, z == 0]
            funcs = [lambda z: tent_map_1(z), lambda z: tent_map_2(z), lambda z: z + random.uniform(0,1)]
            
            z = np.piecewise(z, conds, funcs)

            # Map to original interval
            p = np.interp(z, [0, 1], [self.min_val, self.max_val])
            
            particle = p[:] 
            
            OP = np.copy(particle)

            if self.sim_model != None:
                PV = self.__getTransferFunctionOutput(self.sim_model, OP, self.t2, self.X0) 
            else:
                PV = self.__getSoaOutput(OP) 

            fitness = signalprocessing.cost(self.t2, PV, cost_function_label=self.cost_f, st_importance_factor=self.st_importance_factor, SP=self.SP).costEval

            for j in range(0, self.n):
                if fitness > pbest_value[j]:
                    pbest[j, :] = p[:]

                    pbest_value[j] = fitness 

            if fitness < gbest_cost:   
                gbest[:] = p[:]

                gbest_cost_history = np.append([gbest_cost_history], [fitness[j]])
