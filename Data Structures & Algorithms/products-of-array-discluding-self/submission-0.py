class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1] * (len(nums))

        for i in range(1, len(nums)):
                prefix[i] = prefix [i-1] * nums[i-1]

        postfix = [0] * (len(nums))
        postfix[-1] = 1
        postfix[-2] = nums[-1]

        for i in range(len(postfix)-3, -1, -1):
                postfix[i] = postfix[i+1] * nums[i+1]


        result = [0] * (len(nums))
        for i in range(len(nums)):
            result[i] = prefix[i] * postfix[i] 
        return result   



