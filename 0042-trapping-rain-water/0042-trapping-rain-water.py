class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        lmax, rmax = height[0], height[-1]
        ans = 0
        while i<=j:
            if height[i] > lmax:
                lmax = height[i]
            if height[j] > rmax:
                rmax = height[j]
            if lmax <= rmax:
                ans += lmax - height[i]
                i += 1
            else:
                ans += rmax - height[j]
                j -= 1
        return ans