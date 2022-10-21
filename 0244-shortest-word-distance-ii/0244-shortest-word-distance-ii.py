class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.d = collections.defaultdict(list)
        for i,w in enumerate(wordsDict):
            self.d[w].append(i)
        

    def shortest(self, word1: str, word2: str) -> int:
        return min(abs(n1-n2) for n1 in self.d[word1] for n2 in self.d[word2])
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)