class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res, n = [], len(nums)
        for i in range(n):
            if i>0 and nums[i] == nums[i-1]:
                continue
            target = -1 * nums[i]
            s, e = i+1, n-1
            while s<e:
                twosum = nums[s] + nums[e]
                if twosum == target:
                    res.append([nums[i], nums[s], nums[e]])
                    s += 1
                    while s<e and nums[s] == nums[s-1]:
                        s += 1
                elif twosum < target:
                    s += 1
                else:
                    e -= 1
        return res