class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for word in wordDict:
                if s[i-len(word):i] == word and dp[i-len(word)]:
                    dp[i] = True
        return dp[-1]