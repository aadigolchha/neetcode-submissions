class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        length = 0
        seen = defaultdict(int)

        replacements = 0
        max_char_f = 0
        for r in range(len(s)):
            seen[s[r]] += 1
            max_char_f = max(seen[s[r]], max(seen.values()))
            if (r - l + 1) - max_char_f <= k:
                length = max(length, r - l + 1)
            else:
                seen[s[l]] -= 1
                l += 1
                length = r - l + 1


        return length

                



