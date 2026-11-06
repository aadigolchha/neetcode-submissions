class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        V = {}
        for n in nums:
            if n not in V:
                V[n] = 1
            else: 
                if n + n == target:
                    v1 = nums.index(n)
                    v2 = nums.index(n, v1+1)
                    return [v1, v2]
                V[n] += 1
        
        for n in V:
            if (target - n) in V and (target - n) != n:
                return [min(nums.index(n), nums.index(target-n)), max(nums.index(n), nums.index(target-n))]

        return False