class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        alph = [c for c in s if c.isalpha()]
        return ''.join([s[i] if not s[i].isalpha() else alph.pop() for i in range(len(s))])