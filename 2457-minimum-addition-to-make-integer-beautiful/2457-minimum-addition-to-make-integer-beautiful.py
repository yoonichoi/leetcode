class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def digsum(num):
            return sum([int(d) for d in str(num)])
        
        zeros, add = 10, 0
        while digsum(n+add) > target:
            add = zeros - n%zeros
            zeros *= 10
        return add