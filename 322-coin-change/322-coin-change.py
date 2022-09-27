class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        maxx = float('inf')
        dp = [maxx] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            dp[i] = min(dp[i-c] if i>=c else maxx for c in coins) + 1
        return -1 if dp[-1] == maxx else dp[-1]
        