class TwoSum:

    def __init__(self):
        self.arr = {}
        

    def add(self, number: int) -> None:
        if number in self.arr:
            self.arr[number] += 1
        else:
            self.arr[number] = 1

    def find(self, value: int) -> bool:
        for num in self.arr:
            if value-num in self.arr and (value-num != num or self.arr[num] > 1):
                return True
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)