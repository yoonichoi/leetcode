class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome(s, i, j):
            while i >= 0 and j < len(s) and s[i]==s[j]:
                i -= 1
                j += 1
            return s[i+1:j]
        res = ''
        for i in range(len(s)):
            res = max(res, palindrome(s,i,i), palindrome(s,i,i+1), key=len)
        return res