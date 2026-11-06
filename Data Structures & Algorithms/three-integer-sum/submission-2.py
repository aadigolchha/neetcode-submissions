class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if len(nums) < 3:
            return []

        nums.sort()

        result = []
        for idx, n in enumerate(nums):

            if idx > 0 and n == nums[idx - 1]:
                continue

            target = -1 * n

            l = idx + 1
            r = len(nums) - 1

            while l < r:
                if nums[l] + nums[r] == target:
                    result.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else: 
                    l += 1


        
        return result
