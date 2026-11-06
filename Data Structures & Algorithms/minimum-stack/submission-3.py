class MinStack:

    def __init__(self):
        self.min_val = []
        self.arr = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if not self.min_val or val <= self.min_val[-1]:
            self.min_val.append(val)

    def pop(self) -> None:
        if self.arr[-1] == self.min_val[-1]:
            self.min_val.pop()
        self.arr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        if self.min_val:
            return self.min_val[-1]
        
