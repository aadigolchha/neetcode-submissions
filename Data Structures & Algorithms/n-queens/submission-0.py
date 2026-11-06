class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:

        self.result = []
        self.pos = []
        for j in range(n):
            self.backtrack(self.pos, 0, j, n)

        res_strings = []
        print(self.result)
        for pos in self.result:
            res_list = [n*"." for _ in range(n)]
            for a,b in pos:
                res_list[a] = (b * ".") + "Q" + ((n-b-1) * ".")
            res_strings.append(res_list)
        
        return res_strings

    def backtrack(self, pos, i, j, n):
        
        for entry in self.pos:
            if self.conflict(entry[0], entry[1], i, j):
                return
        
        if len(self.pos) > n:
            return

        self.pos.append((i,j))

        if len(self.pos) == n:
            self.result.append(self.pos.copy())
            self.pos.pop()
            return

        for j in range(n):
            self.backtrack(self.pos, i+1, j, n)
        self.pos.pop()



    def conflict(self, a,b,c,d):

        if a == c or b == d:
            return True

        if abs(a-c) == abs(b-d):
            return True

        return False


        
