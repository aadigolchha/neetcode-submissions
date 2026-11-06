class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)

        curr = []
        for idx, n in enumerate(temperatures):
            while curr and n > curr[-1][0]:
                res[curr[-1][1]] = idx - curr[-1][1]
                curr.pop()
            
            curr.append((n, idx))

        return res

            
        
        