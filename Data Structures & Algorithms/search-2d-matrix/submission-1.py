class Solution:    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for l in matrix:
            if target >= l[0] and target <= l[len(l) - 1]:
                return self.binsearch(l, target)
            
        return False

    def binsearch(self, l: List, target: int) -> bool:

        low = 0
        high = len(l) - 1

        while low <= high:
            mid = (low + high) // 2

            if l[mid] > target:
                high = mid - 1
            elif l[mid] < target: 
                low = mid + 1
            else:
                return True
        return False
