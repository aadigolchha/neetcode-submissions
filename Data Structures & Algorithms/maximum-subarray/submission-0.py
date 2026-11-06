class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums) < 2:
            return nums[0]

        dp = [0] * len(nums)

        dp[0] = nums[0]

        for i in range(1, len(nums)):

            if dp[i-1] > 0:
                dp[i] = dp[i-1] + nums[i]
            else:
                dp[i] = nums[i]

        print(dp)
        return max(dp)
