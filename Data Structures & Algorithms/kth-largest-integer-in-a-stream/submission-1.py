from queue import PriorityQueue
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pq = PriorityQueue()
        self.k = k
        for num in nums:
            self.pq.put(num)
            if self.pq.qsize() > self.k:
                self.pq.get()


    def add(self, val: int) -> int:
        self.pq.put(val)

        if self.pq.qsize() > self.k:
            self.pq.get()

        return self.pq.queue[0]
        
