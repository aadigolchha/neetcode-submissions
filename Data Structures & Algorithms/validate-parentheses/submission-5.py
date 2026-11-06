class Solution:
    def isValid(self, s: str) -> bool:

        if not s: return True 
        if len(s) < 2: return False

        map = {"[" : "]" , "]": "[" , "(" : ")" , ")" : "(" , "{" : "}" , "}" : "{"}
        open = ["(", "{", "["]
        close = [")", "}", "]"]

        arr = []
        for char in s:
            if char in open:
                arr.append(char)
            elif char in close:
                if not arr:
                    return False
                check = arr.pop()
                if char == map[check]:
                    continue
                else:
                    return False

        if arr:
            return False

        return True
        



        

        

        