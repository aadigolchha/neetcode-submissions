class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        pairs = n * 2
        self.result = set()
        self.curstr = ""
        self.backtrack(self.curstr, pairs)
        return list(self.result)

    def backtrack(self, curstr, pairs):

        if len(self.curstr) > pairs:
            return
        
        if len(curstr) == pairs and curstr not in self.result and self.isWellFormed(self.curstr):
            self.result.add(self.curstr)
            return

        self.curstr += "("
        self.backtrack(self.curstr, pairs)
        self.curstr = self.curstr[:-1]

        self.curstr += ")"
        self.backtrack(self.curstr, pairs)
        self.curstr = self.curstr[:-1]

    def isWellFormed(self, curstr):

        stack = []

        for char in curstr:
            if char == "(":
                stack.append(char)

            if char == ")":
                if not stack:
                    return False
                stack.pop()
        
        return not stack


        
