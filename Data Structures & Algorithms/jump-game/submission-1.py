class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if len(nums) == 1:
            return True

        max_index = 0
        dp = [0] * len(nums)

        dp[0] = nums[0]
        max_index = max(dp)
        
        for i in range(len(nums)):
            if i <= max_index:
                dp[i] = i + nums[i]
                max_index = max(max_index, dp[i])
            else:
                return False

        return True