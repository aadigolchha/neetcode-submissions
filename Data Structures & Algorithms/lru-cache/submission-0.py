class LRUCache:

    def __init__(self, capacity: int):
        
        self.cache = defaultdict()
        self.capacity = capacity



    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache[key]
            self.cache.pop(key)
            self.cache[key] = val
            return self.cache[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
        elif len(self.cache.keys()) >= self.capacity:
            LRU = next(iter(self.cache))
            self.cache.pop(LRU)
            self.cache[key] = value
        else:
            self.cache[key] = value
        
        

