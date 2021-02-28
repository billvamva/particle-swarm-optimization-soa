  def regroup(self, x, gbest, v):
      """
      This method regroups the data if premature convergence is found and updates boundaries

      Args:
      - Particle Positions
      - Global Best Positions

      Returns:
      -
      """

      for g in range(0, self.m_c):

          dist = 0

          for j in range(0, self.n):

              dist = max(dist, abs(x[j, g] - gbest[g]))

          self.range_regroup[g] = self.rho * dist

          self.LB[g] = gbest[g] - 0.5 * self.range_regroup[g]
          self.UB[g] = gbest[g] + 0.5 * self.range_regroup[g]

          self.v_LB[g] = - self.lmd * self.range_regroup[g]
          self.v_UB[g] = self.lmd * self.range_regroup[g]

      for j in range(0, self.n):

          for g in range(0, self.m_c):

              x[j, g] = 0.7 * gbest[g] +  0.3 * x[j,g] * v[j,g] + random.uniform(0,1) * self.range_regroup[g] - 0.5 * self.range_regroup[g]
