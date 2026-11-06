class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        self.result = []
        self.curarr = []

        self.backtrack(s)

        strs = []

        for arr in self.result:
            split = []
            start = 0

            for end in arr:
                split.append(s[start:end])
                start = end

            strs.append(split)

        return strs

    def backtrack(self, s):

        start = self.curarr[-1] if self.curarr else 0

        if start == len(s):
            self.result.append(self.curarr.copy())
            return

        for end in range(start + 1, len(s) + 1):
            part = s[start:end]

            if part == part[::-1]:
                self.curarr.append(end)
                self.backtrack(s)
                self.curarr.pop()


    def isPalindromeAll(self, curarr, s):

        split = []
        start = 0

        for idx in curarr:
            split.append(s[start:idx])
            start = idx

        for string in split:
            l = 0
            r = len(string) - 1

            while l < r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1

        return True

