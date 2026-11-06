class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = 0

        for i in range(len(s)):
            count += self.expand_odd(i, s)
            if i+1 < len(s) and s[i] == s[i+1]:
                count += self.expand_even(i,s)
        
        return count


    def expand_odd(self, i, s):

        count = 1
        l = i-1
        r = i+1
        
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            r += 1
            l -= 1

        return count

    def expand_even(self, i, s):

        count = 1
        l = i-1
        r = i+2

        while l >=0 and r < len(s) and s[l] == s[r]:
            count += 1
            r += 1
            l -= 1

        return count

