class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        V = {}
        for idx, n in enumerate(nums):
            if n not in V:
                V[n] = idx
            else: 
                if n + n == target:
                    v1 = nums.index(n)
                    v2 = nums.index(n, v1+1)
                    return [v1, v2]
        
        for n in V:
            if (target - n) in V and (target - n) != n:
                return [V[n], V[target - n]]

        return False