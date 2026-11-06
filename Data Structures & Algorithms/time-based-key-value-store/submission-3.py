class TimeMap:

    def __init__(self):
        self.map = defaultdict(dict)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key][int(timestamp)] = value 


    def get(self, key: str, timestamp: int) -> str:
        
        arr = list(self.map[key].keys())

        time = self.binsearch(arr, timestamp)

        if time != -1:
            return self.map[key][time]
        else:
            return ""

    
    def binsearch(self, l: List, target: int) -> int:

        low = 0
        high = len(l) - 1
        lowest = -1
        while low <= high:
            mid = (low + high) // 2

            if l[mid] > target:
                high = mid - 1
            elif l[mid] < target:
                lowest = l[mid] 
                low = mid + 1
            else:
                return l[mid]
        return lowest
