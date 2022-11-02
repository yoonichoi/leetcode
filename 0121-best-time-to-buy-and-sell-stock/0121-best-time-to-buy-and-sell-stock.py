class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, maxx = 0, 1, 0
        while r < len(prices):
            if prices[r] > prices[l]:
                maxx = max(maxx, prices[r]-prices[l])
            else:
                l = r
            r += 1
        return maxx