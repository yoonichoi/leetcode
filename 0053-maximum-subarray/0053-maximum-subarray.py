class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i, num in enumerate(nums):
            dp[i] = max(num, dp[i-1]+num)
        return max(dp)