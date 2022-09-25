class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = curr = 0
        for num in nums:
            tmp = prev
            prev = curr
            curr = max(num+tmp, prev)
        return curr
    