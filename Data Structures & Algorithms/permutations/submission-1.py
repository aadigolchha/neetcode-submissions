class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        self.res, self.curr = [], []
        self.backtrack(0, nums)
        return self.res

    def backtrack(self, i, nums):

        if len(self.curr) == len(nums):
            self.res.append(self.curr.copy())
            return

        if i >= len(nums):
            return

        for i in range(len(nums)):
            if nums[i] not in self.curr:
                self.curr.append(nums[i])
                self.backtrack(i, nums)
                self.curr.pop()

        self.backtrack(i+1, nums)
