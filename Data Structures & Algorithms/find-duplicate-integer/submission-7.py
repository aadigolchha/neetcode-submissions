class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        S = 0
        F = 0

        while True:
            S = nums[S]
            F = nums[nums[F]]

            if S == F:
                break
        
        S2 = 0
        while S != S2:
            S = nums[S]
            S2 = nums[S2]

        return S

