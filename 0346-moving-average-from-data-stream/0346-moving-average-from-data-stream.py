class MovingAverage:

    def __init__(self, size: int):
        import collections
        self.lst = collections.deque()
        self.sum = 0
        self.size = size
        

    def next(self, val: int) -> float:
        self.lst.append(val)
        if len(self.lst) > self.size:
            self.sum -= self.lst.popleft()
        self.sum += val
        return self.sum / len(self.lst)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)