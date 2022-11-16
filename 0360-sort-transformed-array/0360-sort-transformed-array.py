class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def quad(x):
            return a*x**2 + b*x + c
        n = len(nums)
        res = [0] * n
        l, r = 0, n-1
        idx = 0 if a < 0 else n-1
        while l<=r:
            lv, rv = quad(nums[l]), quad(nums[r])
            if a < 0:
                if lv < rv:
                    res[idx] = lv
                    l += 1
                else:
                    res[idx] = rv
                    r -= 1
                idx += 1
            else:
                if lv < rv:
                    res[idx] = rv
                    r -= 1
                else:
                    res[idx] = lv
                    l += 1
                idx -= 1
        return res