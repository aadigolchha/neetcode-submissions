class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operators = ["+", "-", "*", "/"]

        arr = []

        for token in tokens:
            if token in operators:
                if len(arr) < 2:
                    return -1
                if token == "+":
                    p1 = int(arr.pop())
                    p2 = int(arr.pop())
                    arr.append(p1 + p2)         
                elif token == "-":
                    p1 = int(arr.pop())
                    p2 = int(arr.pop())
                    arr.append(p2 - p1)
                elif token == "*":
                    p1 = int(arr.pop())
                    p2 = int(arr.pop())
                    arr.append(p1 * p2)
                elif token == "/":
                    p1 = int(arr.pop())
                    p2 = int(arr.pop())
                    arr.append(p2 / p1)
            else:
                arr.append(token)
        
        if len(arr) > 1:
            return -1
        return int(arr[0])

        

                


