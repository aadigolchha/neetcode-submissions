class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if len(nums) == 1:
            return True

        max_index = nums[0]

        for i in range(len(nums)):
            if i <= max_index:
                max_index = max(max_index, i+nums[i])
            else:
                return False

        return True