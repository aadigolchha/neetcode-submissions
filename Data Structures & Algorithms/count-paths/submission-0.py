class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0 for _ in range(n)]for _ in range(m)]

        for i in range(len(dp[0])):
            dp[0][i] = 1

        for i in range(len(dp)):
            dp[i][0] = 1

        for row in range(1, len(dp)):
            for col in range(1, len(dp[0])):
                if dp[row][col] == 0:
                    dp[row][col] = dp[row - 1][col] + dp[row][col-1]
        
        
        return dp[m-1][n-1]
