class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) == 0:
            return []

        self.digits_to_char = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }

        self.result = set()
        self.curstr = ""
        self.backtrack(digits, self.curstr, 0)

        return list(self.result)

        
    def backtrack(self, digits, curstr, i):

        if len(self.curstr) == len(digits) and self.curstr not in self.result:
            self.result.add(self.curstr)
            return

        if len(self.curstr) > len(digits) or i >= len(digits):
            return

        for char in self.digits_to_char[digits[i]]:
            self.curstr += char
            self.backtrack(digits, self.curstr, i+1)
            self.curstr = self.curstr[:-1]
            

        
        
            