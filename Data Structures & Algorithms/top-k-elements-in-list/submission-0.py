from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        map = defaultdict(int)
        for n in nums:
            map[n] += 1

        listed = sorted(map.items(), key=lambda item: item[1])
        listed.reverse()


        result = []
        for i in range(k):
            result.append(listed[i][0])
        
        return result


