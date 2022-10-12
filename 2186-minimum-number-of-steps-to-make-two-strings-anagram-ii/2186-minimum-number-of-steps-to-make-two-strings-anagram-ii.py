class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dic = {}
        for c in s:
            dic[c] = dic.get(c,0) + 1
        for c in t:
            dic[c] = dic.get(c,0) - 1
        cnt = 0
        for k,v in dic.items():
            cnt += abs(v)
        return cnt