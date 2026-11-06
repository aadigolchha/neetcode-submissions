class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        s_chars = {}
        for char in s:
            if char in s_chars.keys():
                s_chars[char] += 1
            else:
                s_chars[char] = 1
        
        t_chars = {}
        for char in t:
            if char in t_chars.keys():
                t_chars[char] += 1
            else:
                t_chars[char] = 1

        if len(s_chars.keys()) != len(t_chars.keys()):
            return False

        for key in s_chars.keys():
            if key not in t_chars.keys() or s_chars[key] != t_chars[key]:
                return False

        return True

