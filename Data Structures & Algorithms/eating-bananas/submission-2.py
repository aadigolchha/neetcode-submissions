class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        piles.sort()
        num_piles = len(piles)
        num_b = sum(piles)

        low = 1
        high = piles[-1]

        lowest = 0
        while low <= high:

            mid = (low + high) // 2

            if self.hours(piles, mid) > h:
                low = mid + 1
            
            elif self.hours(piles, mid) <= h:
                lowest = mid
                high = mid - 1
        
        return lowest


    def hours (self, piles: List[int], k: int) -> int:
        sum = 0
        for pile in piles:
            sum += (pile + k - 1) // k
        
        return sum
