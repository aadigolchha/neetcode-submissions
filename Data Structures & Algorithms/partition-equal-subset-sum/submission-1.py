class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2 != 0:
            return False

        nums = sorted(nums)
        total = sum(nums)
        target = total // 2
        
        dp = [False for _ in range(target + 1)]
        dp[0] = True

        for i in range(len(nums)):
            for j in range(target, i, -1):

                if dp[j - nums[i]]:
                    dp[j] = True 
        

        return dp[target]
            

        


