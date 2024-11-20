class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}

        def climbStairsRecurse(n: int) -> int:
            if n == 1:
                return 1
            
            if n == 2:
                return 2
            
            oneStepBack = climbStairsRecurse(n - 1) if n - 1 not in memo else memo[n - 1]
            twoStepsBack = climbStairsRecurse(n - 2) if n - 2 not in memo else memo[n - 2]
            totalNumberOfWays = oneStepBack + twoStepsBack
            memo[n] = totalNumberOfWays
            return totalNumberOfWays
        
        return climbStairsRecurse(n)

"""

0 + 1 + 1
      + 2
  + 2 + 1
      + 2

n = 3

previous steps could have been from as long as valid

think of number of ways to reach n - 1th step climbStairs(n - 1)
think of number of ways to reach n - 2nd step climbStairs(n - 2) and you add them
as long as n - 1 > =1.

Ok so the intuition is there. And it works. But it's too slow. Need to improve on the time complexity.

How to do that? Use memoization.

Ok, so what am I supposed to memoize? Remember how many ways there are to reach every nth step.
"""
