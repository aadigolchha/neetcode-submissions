class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        pops = 0
        last_end = float('-inf')
        
        for start, end in intervals:
            if start < last_end:
                pops += 1
            else:
                last_end = end
                
        return pops