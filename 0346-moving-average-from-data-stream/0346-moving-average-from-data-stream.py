class MovingAverage:

    def __init__(self, size: int):
        self.lst = []
        self.size = size
        

    def next(self, val: int) -> float:
        self.lst.append(val)
        if len(self.lst) < self.size:
            return sum(self.lst)/len(self.lst)
        else:
            return sum(self.lst[-1*self.size:])/self.size

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)