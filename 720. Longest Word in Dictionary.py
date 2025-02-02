class Node:
    def __init__(self, char=''):
        self.char = char
        self.end = False
        self.children = dict()
class Trie:
    def __init__(self):
        self.root = Node('')
    def insert(self,word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node(c)
            curr = curr.children[c]
        curr.end = True
    def search(self,word):
        curr = self.root
        for c in word:
            curr = curr.children[c]
            if not curr.end:
                return False
        return True

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        words.sort(key = lambda x: (-len(x),x))

        for word in words:
            if trie.search(word):
                return word
        return ''
        