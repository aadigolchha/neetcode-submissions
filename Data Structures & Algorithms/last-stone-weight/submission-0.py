from queue import PriorityQueue

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        pq = PriorityQueue()

        for num in stones:
            pq.put(-1*num)

        while pq.qsize() > 1:
            i1 = pq.get() * -1
            i2 = pq.get() * -1
            if i1 > i2:
                pq.put(-1 * (i1-i2))
        
        if pq.qsize() == 0:
            return 0
        else:
            return pq.get() * -1