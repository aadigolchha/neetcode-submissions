class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        self.res, self.curr = set(), []
        self.backtrack(0, nums)
        result = []
        for t in self.res:
            result.append(list(t))
        return result

    def backtrack(self, i, nums):

        if tuple(self.curr) not in self.res:
            self.res.add(tuple(self.curr))

        if i >= len(nums):
            return

        self.curr.append(nums[i])
        self.backtrack(i+1, nums)
        self.curr.pop()

        self.backtrack(i+1, nums)
        
