class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if len(nums) < 2:
            return nums[0]

        dp = [(0,0)] * len(nums)

        dp[0] = (nums[0], nums[0])

        for i in range(1, len(nums)):

            dp[i] = (
                min(nums[i], dp[i-1][1] * nums[i], dp[i-1][0] * nums[i]),
                max(nums[i], dp[i-1][1] * nums[i], dp[i-1][0] * nums[i])
            )
        
        dp = [item[1] for item in dp]
        return max(dp)

