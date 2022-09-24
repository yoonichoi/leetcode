class WordNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:
    def __init__(self):
        self.root = WordNode()
        
    def addWord(self, word):
        node = self.root
        for w in word:
            if w in node.children:
                node = node.children[w]
            else:
                node.children[w] = WordNode()
                node = node.children[w]
        node.isEnd = True
                
    def search(self, word):
        stack = [(self.root,word)]
        while stack:
            node, w = stack.pop()
            if not w:
                if node.isEnd:
                    return True
            elif w[0]=='.':
                for n in node.children.values():
                    stack.append((n,w[1:]))
            else:
                if w[0] in node.children:
                    n = node.children[w[0]]
                    stack.append((n,w[1:]))
        return False
# class TrieNode:
#     def __init__(self):
#         self.dict = {}
#         self.word = False
        
# class WordDictionary(object):

#     def __init__(self):
#         self.root = TrieNode()

#     def addWord(self, word):
#         """
#         :type word: str
#         :rtype: None
#         """
#         node = self.root
#         for c in word:
#             if c in node.dict:
#                 node = node.dict[c]
#             else:
#                 node.dict[c] = TrieNode()
#                 node = node.dict[c]
#         node.word = True

#     def search(self, word):
#         """
#         :type word: str
#         :rtype: bool
#         """
#         stack = [(self.root, word)]
#         while stack:
#             node, w = stack.pop()
#             if not w and node.word:
#                 return True
#             elif w[0] == '.':
#                 for n in node.dict.values():
#                     stack.append((n, w[1:]))
#             else:
#                 if w[0] in node.dict:
#                     n = node.dict[w[0]]
#                     stack.append((n, w[1:]))
#         return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)