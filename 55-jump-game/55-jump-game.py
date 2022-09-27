class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reachable = 0
        for curr in range(len(nums)):
            if curr + nums[curr] >= reachable:
                reachable = curr+nums[curr]
            if curr == reachable:
                break
        return reachable >= len(nums)-1
        