class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        
        self.res, self.curset = [], []
        self.backtrack(0, candidates, self.res, self.curset, target)
        return self.res

    def backtrack(self, i, candidates, res, curset, target):

        if sum(self.curset) == target:
            self.res.append(self.curset.copy())
            return
        if sum(self.curset) > target:
            return
        if i > len(candidates) - 1:
            return

        self.curset.append(candidates[i])
        self.backtrack(i, candidates, self.res, self.curset, target)
        self.curset.pop()

        self.backtrack(i + 1, candidates, self.res, self.curset, target)