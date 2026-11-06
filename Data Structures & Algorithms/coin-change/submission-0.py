class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        coins = sorted(coins)

        if amount == 0:
            return 0
        
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
        
        for i in range(amount + 1):
            
            if dp[i] == 1:
                continue

            for coin in coins:
                if i - coin >= 0 and dp[i - coin] != -1:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        
        if dp[-1] == amount + 1:
            return -1
        else:
            return dp[-1]

