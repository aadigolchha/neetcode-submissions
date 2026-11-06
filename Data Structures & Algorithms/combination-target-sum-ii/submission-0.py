class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        self.res, self.CurSum = [], []
        candidates = sorted(candidates)

        self.backtrack(0, self.CurSum, candidates, target)

        return self.res

    def backtrack(self, i, CurSum, candidates, target):

        if sum(self.CurSum) > target:
            return
        
        if sum(self.CurSum) == target:
            self.res.append(self.CurSum.copy())
            return
        
        if i >= len(candidates):
            return

        self.CurSum.append(candidates[i])
        self.backtrack(i+1, self.CurSum, candidates, target)        
        self.CurSum.pop()

        while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
            i += 1

        self.backtrack(i+1, self.CurSum, candidates, target)

