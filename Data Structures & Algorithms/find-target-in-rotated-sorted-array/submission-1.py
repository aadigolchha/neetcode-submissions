class Solution:
    def search(self, nums: List[int], target: int) -> int:
    
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            if nums[mid] > nums[high]:
                low = mid + 1
            elif nums[mid] < nums[high]:
                high = mid

        pivot = low
        arr = nums[pivot:] + nums[:pivot]
        
        res = self.binsearch(arr, target)
        if res == -1:
            return -1
        else:
            return (res + pivot) % len(nums)

    def binsearch(self, l: List, target: int) -> int:

        low = 0
        high = len(l) - 1

        while low <= high:
            mid = (low + high) // 2

            if l[mid] > target:
                high = mid - 1
            elif l[mid] < target: 
                low = mid + 1
            else:
                return mid
        return -1