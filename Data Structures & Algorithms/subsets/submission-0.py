class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        self.res, self.curset = [], []
        self.backtrack(0, nums, self.curset)
        return(self.res)

    def backtrack(self, i , nums, curset):

        if self.curset not in self.res:
            self.res.append(self.curset.copy())

        if i >= len(nums):
            return
        
        self.curset.append(nums[i])
        self.backtrack(i+1, nums, self.curset)
        self.curset.pop()

        self.backtrack(i+1, nums, self.curset)

