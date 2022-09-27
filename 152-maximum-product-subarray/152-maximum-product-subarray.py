class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curmax, curmin = 1, 1
        res = nums[0]
        for n in nums:
            vals = (n, n * curmax, n * curmin)
            curmax, curmin = max(vals), min(vals)
            res = max(curmax, res)
        return res