class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for idx, num in enumerate(nums):
            if (target - num) in seen:
                return (idx, seen[target-num])
            else:
                seen[num] = idx