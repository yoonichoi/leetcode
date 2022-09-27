class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ''
        leng = 0
        for i in range(len(s)):
            # odd
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 >= leng:
                    ans = s[l:r+1]
                    leng = r - l + 1
                l -= 1
                r += 1
            #even
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 >= leng:
                    ans = s[l:r+1]
                    leng = r - l + 1
                l -= 1
                r += 1
        return ans
            