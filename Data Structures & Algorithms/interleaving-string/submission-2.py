class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False

        if len(s3) == 1 and s1 != s3 and s2 != s3:
            return False

        d1 = {}
        d2 = {}

        d1[0] = set()
        d2[0] = set()

        d1[0].add((s1, s2))
        d2[0].add((s1, s2))

        for i in range(1, len(s3)+1):

            d1[i] = set()
            d2[i] = set()

            char = s3[i-1]
            
            for pair in d1[i-1]:
                if len(pair[0]) >= 1 and pair[0][0] == char:
                    d1[i].add((pair[0][1:], pair[1]))
                if len(pair[1]) >= 1 and pair[1][0] == char:
                    d2[i].add((pair[0], pair[1][1:]))
            for pair in d2[i-1]:
                if len(pair[0]) >= 1 and pair[0][0] == char:
                    d1[i].add((pair[0][1:], pair[1]))
                if len(pair[1]) >= 1 and pair[1][0] == char:
                    d2[i].add((pair[0], pair[1][1:]))
            if len(d1[i]) == 0 and len(d2[i]) == 0:
                return False

        print(d1)
        print(d2)

        return True
                        


