class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        map_s1 = defaultdict(int)
        for char in s1:
            map_s1[char] += 1

        L = 0
        R = len(s1)

        for char in s2[L:R]:
            map_s1[char] -= 1

        while R < len(s2):
            
            if all(v == 0 for v in map_s1.values()):
                return True

            else:
                map_s1[s2[L]] += 1
                map_s1[s2[R]] -= 1
                L += 1
                R += 1
            
        if all(v == 0 for v in map_s1.values()):
            return True
        return False            

