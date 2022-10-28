class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = [i for i in s if i.isalnum()]
        s = ''.join(s)
        return s == s[::-1]