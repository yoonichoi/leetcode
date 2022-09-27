class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curmax, allmax = 0, float('-inf')
        for n in nums:
            curmax = max(n,curmax+n)
            allmax = max(curmax,allmax)
        return allmax
        
        
        