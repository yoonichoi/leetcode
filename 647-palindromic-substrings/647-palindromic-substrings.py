class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        
        n = len(s)
        cnt = 0
        dp = [[False for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = True
            cnt += 1
        
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                cnt += 1
        
        for k in range(3, n+1):
            for i in range(n-k+1):
                j = i+k-1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    cnt += 1
        return cnt