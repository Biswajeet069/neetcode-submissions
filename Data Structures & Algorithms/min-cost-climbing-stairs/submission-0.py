class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)
        s = [-1] * (n + 1)

        def dp(index):

            if index >= n:
                return 0

            if s[index] != -1:
                return s[index]

            s[index] = cost[index] + min(dp(index + 1), dp(index + 2))

            return s[index]

        return min(dp(0), dp(1))
        
        