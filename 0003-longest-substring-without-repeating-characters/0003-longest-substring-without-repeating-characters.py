class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxx, start = 0, 0
        seen = {}
        for i, c in enumerate(s):
            if c in seen and start <= seen[c]:
                start = seen[c] + 1
            else:
                maxx = max(maxx, i-start+1)
            seen[c] = i
        return maxx