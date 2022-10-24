class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        # enumerate and store in dict
        dic = collections.defaultdict(list)
        for pos, word in enumerate(wordsDict):
            dic[word].append(pos)
        return min(abs(n1-n2) for n1 in dic[word1] for n2 in dic[word2])