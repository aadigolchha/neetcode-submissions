from queue import PriorityQueue
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pq = PriorityQueue()
        for num in nums:
            self.pq.put(-1 * num)
        self.k = k

    def add(self, val: int) -> int:
        self.pq.put(-1 * val)

        tmp = []
        for _ in range(self.k):
            tmp.append(self.pq.get())

        res = -1 * tmp[-1]

        for num in tmp:
            self.pq.put(num)

        return res
        
