class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if len(nums) < 3:
            return []

        nums.sort()

        result = set()
        for idx, n in enumerate(nums):

            if n != nums[-1]:
                nums2 = nums[:idx] + nums[idx+1:]
            else:
                nums2 = nums[:idx]
            
            target = -1 * n

            l = 0
            r = len(nums2) - 1

            while l < r:
                if nums2[l] + nums2[r] == target:
                    result.add((n, nums2[l], nums2[r]))
                    l += 1
                    r -= 1
                elif nums2[l] + nums2[r] > target:
                    r -= 1
                else: 
                    l += 1
        
        result2 = []
        for s in result:
            s = list(s)
            s.sort()
            if s not in result2:
                result2.append(s)

        
        return result2
