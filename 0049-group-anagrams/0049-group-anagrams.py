class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for w in strs:
            dic[str(sorted(w))].append(w)
        ans = []
        for i,v in dic.items():
            ans.append(v)
        return ans