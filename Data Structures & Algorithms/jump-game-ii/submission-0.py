class Solution:
    def jump(self, nums: List[int]) -> int:
        
        jumps = 0
        pos = 0

        while pos < len(nums) - 1:

            if pos + nums[pos] >= len(nums) - 1:
                return jumps + 1
            
            best, best_idx = 0,0
            l = pos + 1
            r = pos + nums[pos]
            candidates = nums[l:r + 1]

            for idx, n in enumerate(candidates):
                if pos + idx + 1 + n > best:
                    best = pos + idx + 1 + n
                    best_idx = idx
            
            pos = pos + best_idx + 1
            jumps += 1

        return jumps