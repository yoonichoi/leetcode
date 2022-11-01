class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, ans = 0, 0
        seen = {}
        for r in range(len(s)):
            if s[r] not in seen:
                ans = max(ans, r-l+1)
            else:
                if seen[s[r]] < l:
                    ans = max(ans, r-l+1)
                else:
                    l = seen[s[r]] + 1
            seen[s[r]] = r
        return ans