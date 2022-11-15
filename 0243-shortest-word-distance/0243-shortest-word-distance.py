class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        d = collections.defaultdict(list)
        for i, w in enumerate(wordsDict):
            d[w].append(i)
        return min(abs(n1-n2) for n1 in d[word1] for n2 in d[word2])