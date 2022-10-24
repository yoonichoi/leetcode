class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def quad(x):
            return a*x**2 + b*x + c
        n = len(nums)
        index = 0 if a < 0 else n-1
        l, r, res = 0, n-1, [0]*n
        while l <= r:
            lv, rv = quad(nums[l]), quad(nums[r])
            if a>=0:
                if lv > rv:
                    res[index] = lv
                    l += 1
                else:
                    res[index] = rv
                    r -= 1
                index -= 1
            else:
                if lv > rv:
                    res[index] = rv
                    r -= 1
                else:
                    res[index] = lv
                    l += 1
                index += 1
        return res