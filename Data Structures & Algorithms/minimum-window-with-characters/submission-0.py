class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        l = 0
        r = 0

        t_chars = {}
        for char in t:
            if char not in t_chars:
                t_chars[char] = 1
            else: t_chars[char] += 1
        t_len = len(t)
        first_char = True

        min_l = 0
        min_r = 100000

        curr = {}
        match = 0
        while r < len(s):
            
            if s[r] in t_chars:
                if s[r] not in curr:
                    curr[s[r]] = 1
                else: curr[s[r]] += 1

                if curr[s[r]] == t_chars[s[r]]:
                    match += 1
            
            if match == len(t_chars.keys()):
                while s[l] not in t_chars or curr[s[l]] > t_chars[s[l]]:
                    if s[l] in curr:
                        curr[s[l]] -= 1
                    l += 1

                if r - l < min_r - min_l:
                    min_l, min_r = l, r

            r += 1
                
        
        if min_r - min_l == 100000:
            return ""
        return s[min_l:min_r+1]
                

            

            