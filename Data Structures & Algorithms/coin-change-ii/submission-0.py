class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [[0 for _ in range(len(coins))]for _ in range(amount+1)]

        dp[0] = [1 for _ in range(len(coins))]

        for n in range(1, amount + 1):
            for idx, coin in enumerate(coins):
                if idx > 0:
                    dp[n][idx] = dp[n][idx - 1]

                if n >= coin:
                    dp[n][idx] += dp[n - coin][idx]

        return dp[amount][-1]

