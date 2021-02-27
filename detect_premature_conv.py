  def detect_regroup(self, x, pbest, pbest_value, gbest, gbest_cost, gbest_cost_history, curr_iter):
      """
      This method determines if regrouping is required to avoid premature convergence

      Args:
      - Particle Positions
      - Global Best Position
      - Current Iteration

      Returns
      - True if Regrouping is required
      """
      for i in range(0, self.n):

          distance = np.linalg.norm(x[i]-gbest)/self.num_points

          if distance > self.swarm_radius[curr_iter - 1]:
              self.swarm_radius[curr_iter - 1] = distance

      self.d_norm[curr_iter - 1] = self.swarm_radius[curr_iter - 1]/(self.max_val - self.min_val)


      if self.d_norm[curr_iter - 1] < 6e-3/self.r:
          print('Chaotic Search Started')
          self.chaotic_search( x, pbest, pbest_value, gbest, gbest_cost, gbest_cost_history, curr_iter)
          self.r = self.r * np.exp
          print('Chaotic Mapping Performed')
