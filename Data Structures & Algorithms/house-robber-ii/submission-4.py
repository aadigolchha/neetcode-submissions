class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) < 2:
            return nums[0]
        
        s1 = 0
        s2 = 0

        dp = [0 for _ in range(len(nums) + 1)]        
        dp[0] = 0
        dp[1] = nums[0]
        dp[2] = max(nums[0], nums[1])

        for i in range(3, len(nums)):
            dp[i] = max(dp[i-2] + nums[i-1], dp[i-1])

        s1 = max(dp)
        print(dp)

        dp = [0 for _ in range(len(nums) + 1)]        
        dp[0] = 0
        dp[1] = 0
        dp[2] = nums[1]

        for i in range(3, len(nums)+1):
            dp[i] = max(dp[i-2] + nums[i-1], dp[i-1])
        
        s2 = max(dp)
        print(dp)
        return max(s1,s2)


            
            