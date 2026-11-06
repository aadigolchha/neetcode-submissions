class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        if len(cost) < 3:
            return min(cost[0], cost[1])

        dp = [[0] for _ in range(len(cost))]

        dp[0] = 0
        dp[1] = 0

        for i in range(2, len(cost)):
            option_1 = dp[i-2] + cost[i-2]
            option_2 = dp[i-1] + cost[i-1]
            dp[i] = min(option_1, option_2)

        return min(dp[-1] + cost[-1], dp[-2] + cost[-2])
