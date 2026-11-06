class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) < 1:
            return s

        dp = s[0] 

        for i in range(len(s)):
            biggest = len(dp)

            odd_count = 1
            while i - odd_count >= 0 and i + odd_count < len(s) and s[i-odd_count] == s[i+odd_count]:
                odd_count += 1

            if i + 1 < len(s) and s[i] == s[i + 1]:
                even_count = 2
                while (
                    i - even_count + 1 >= 0
                    and i + even_count < len(s)
                    and s[i - even_count + 1] == s[i + even_count]
                ):
                    even_count += 1
            else:
                even_count = 1
            
            if 2 * odd_count - 1 > biggest:
                r = odd_count - 1
                dp = s[i-r:i+r+1]
                biggest = len(dp)

            if 2 * even_count - 2 > biggest:
                r = even_count - 1
                dp = s[i-r+1:i+r+1]
        return dp
            
            
             



"""
    def isPalindrome(self, s):

        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True 
        """