class Block:
    def __init__(self, val=0):
        self.val = val
        self.keys = set()
        self.before = None
        self.after = None
    def remove(self):
        self.before.after = self.after
        self.after.before = self.before
        self.before, self.after = None, None
    def insert_after(self, new_block):
        old_after = self.after
        self.after = new_block
        new_block.before = self
        new_block.after = old_after
        old_after.before = new_block
        
class AllOne:
    def __init__(self):
        self.begin = Block()
        self.end = Block()
        self.begin.after = self.end
        self.end.before = self.begin
        self.mapping = {}

    def inc(self, key: str) -> None:
        if not key in self.mapping:
            curr = self.begin
        else:
            curr = self.mapping[key]
            curr.keys.remove(key)
        if curr.val + 1 != curr.after.val:
            new = Block(curr.val+1)
            curr.insert_after(new)
        else:
            new = curr.after
        new.keys.add(key)
        self.mapping[key] = new
        if not curr.keys and curr.val != 0:
            curr.remove()

    def dec(self, key: str) -> None:
        if not key in self.mapping:
            return
        curr = self.mapping[key]
        self.mapping.pop(key)
        curr.keys.remove(key)
        if curr.val != 1:
            if curr.val - 1 != curr.before.val:
                new = Block(curr.val - 1)
                curr.before.insert_after(new)
            else:
                new = curr.before
            new.keys.add(key)
            self.mapping[key] = new
        if not curr.keys:
            curr.remove()

    def getMaxKey(self) -> str:
        if self.end.before.val == 0:
            return ""
        key = self.end.before.keys.pop()
        self.end.before.keys.add(key)
        return key

    def getMinKey(self) -> str:
        if self.begin.after.val == 0:
            return ""
        key = self.begin.after.keys.pop()
        self.begin.after.keys.add(key)
        return key


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()