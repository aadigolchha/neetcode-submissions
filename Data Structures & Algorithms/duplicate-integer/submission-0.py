class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen.keys():
                return True
            else:
                seen[nums[i]] = True
            
        return False