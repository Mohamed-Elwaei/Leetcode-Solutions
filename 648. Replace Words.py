class Node:
    def __init__(self,char=''):
        self.char = char
        self.end,self.children = False, dict()

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

    def search(self, word):
        curr = self.root
        prefix = ''
        for c in word:
            if curr.end:
                return prefix
            elif c not in curr.children:
                return ''
            curr = curr.children[c]
            prefix+=c
        return prefix if curr.end else ''
            


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        
        sentence = sentence.split()
        for i,word in enumerate(sentence):
            root = trie.search(word) or word
            sentence[i] = root
        return ' '.join(sentence)
        