class Solution:
    def isPalindrome(self, s: str) -> bool:

        L = 0
        R = len(s) - 1

        s = s.lower()
        s = s.strip()

        while L < R:    
            if not s[R].isalnum():
                while not s[R].isalnum() and L < R:
                    R -= 1
            if not s[L].isalnum() and L < R:
                while not s[L].isalnum():
                    L += 1

            if s[L] == s[R]:
                L += 1
                R -= 1
            else:
                return False
        return True

        