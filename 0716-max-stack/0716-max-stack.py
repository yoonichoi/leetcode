import heapq

class MaxStack:

    def __init__(self):
        self.ls = []
        self.hp = []
        self.lsd = set()
        self.hpd = set()
        self.idx = 0

    def push(self, x: int) -> None:
        self.ls.append((x, self.idx))
        heappush(self.hp, (-x, -self.idx))
        self.idx += 1

    def pop(self) -> int:
        x = self.top()
        self.hpd.add(self.ls[-1][1])
        self.ls.pop()
        return x
        
    def top(self) -> int:
        while self.ls[-1][1] in self.lsd:
            self.lsd.remove(self.ls[-1][1])
            self.ls.pop()
        return self.ls[-1][0]

    def peekMax(self) -> int:
        while -self.hp[0][1] in self.hpd:
            self.hpd.remove(-self.hp[0][1])
            heappop(self.hp)
        return -self.hp[0][0]

    def popMax(self) -> int:
        x = self.peekMax()
        _, nid = heappop(self.hp)
        self.lsd.add(-nid)
        return x
            


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()