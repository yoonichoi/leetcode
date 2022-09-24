class TrieNode:
    def __init__(self):
        self.dict = {}
        self.word = False
        
class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for c in word:
            if c not in node.dict:
                node.dict[c] = TrieNode()
            node = node.dict[c]
        node.word = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        stack = [(self.root,word)]
        while stack:
            node, w = stack.pop()
            if not w:
                if node.word:
                    return True
            elif w[0]=='.':
                for n in node.dict.values():
                    stack.append((n,w[1:]))
            else:
                if w[0] in node.dict:
                    n = node.dict[w[0]]
                    stack.append((n,w[1:]))
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)