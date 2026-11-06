class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        
        wordDict = set(wordDict)

        if s in wordDict or not s:
            return True

        starting_points = [0]
        temp = []

        for i in range(1, len(s)+1):
            for idx in starting_points:
                if s[idx:i] in wordDict and i not in starting_points:
                    starting_points.append(i)
                    if i == len(s):
                        return True



        return False     
            
        

