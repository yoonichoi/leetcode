class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs = [list(s) for s in strs]
        res = ''
        for chars in zip(*strs):
            if len(set(chars)) == 1:
                res += chars[0]
            else:
                break
        return res