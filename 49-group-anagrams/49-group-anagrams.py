class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for word in strs:
            sortword = ''.join(sorted(word))
            if sortword not in dic:
                dic[sortword] = [word]
            else:
                dic[sortword].append(word)
        return dic.values()