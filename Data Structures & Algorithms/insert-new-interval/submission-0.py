class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        p = 0
        while p < len(intervals) and intervals[p][0] < newInterval[0]:
            p += 1

        intervals.insert(p, newInterval)

        intervals, p = self.collapse_back(intervals, p)
        intervals = self.collapse_forward(intervals, p)

        return intervals

    def collapse_back(self, intervals, p):
        
        while p > 0 and self.isOverlap(intervals[p-1], intervals[p]):
            low = min(intervals[p][0], intervals[p-1][0])
            high = max(intervals[p][1], intervals[p-1][1])
            intervals[p] = [low, high]
            intervals.pop(p-1)
            p -= 1

        return intervals, p


    def collapse_forward(self, intervals, p):
        
        while p < len(intervals) - 1 and self.isOverlap(intervals[p], intervals[p+1]):
            low = min(intervals[p][0], intervals[p+1][0])
            high = max(intervals[p][1], intervals[p+1][1])
            intervals[p] = [low, high]
            intervals.pop(p+1)
        return intervals

    def isOverlap(self, list1, list2):
        return max(list1[0], list2[0]) <= min(list1[1], list2[1])