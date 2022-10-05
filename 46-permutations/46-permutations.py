class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(nums, path, res):
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                helper(nums[:i]+nums[i+1:], path+[nums[i]], res)
        res = []
        helper(nums, [], res)
        return res