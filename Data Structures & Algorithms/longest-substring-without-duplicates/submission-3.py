class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0

        seen = set()
        l = 0
        seen.add(s[l])
        max_length = 1
        length = 1

        for r in range(1, len(s)):
            if s[r] not in seen:
                seen.add(s[r])
                length = r - l + 1
                max_length = max(length, max_length)
            else: 
                while s[r] in seen:
                    seen.discard(s[l])
                    l += 1
                length = r - l + 1
                seen.add(s[r])
                
        return max_length



