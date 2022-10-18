class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        def reverse(n):
            return int(str(n)[::-1])
        return num == reverse(reverse(num))