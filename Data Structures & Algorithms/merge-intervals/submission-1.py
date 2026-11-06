class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x:x[0])

        i = 0
        while i < len(intervals) - 1:
            if self.isOverlap(intervals[i], intervals[i+1]):
                low = min(intervals[i][0], intervals[i+1][0])
                high = max(intervals[i][1], intervals[i+1][1])
                intervals[i] = [low, high]
                intervals.pop(i+1)
            else:
                i += 1

        return intervals
        
        

    def isOverlap(self, list1, list2):
        return max(list1[0], list2[0]) <= min(list1[1], list2[1])

        