class Node:
    def __init__(self, char=''):
        self.char = char
        self.children = dict()
        self.end = False
class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node(c)
            curr = curr.children[c]
        curr.end = 1
        return None
        



    def search(self, word: str) -> bool:
        def aux(word, root):
            for i,c in enumerate(word):
                if c != '.':
                    if c not in root.children:
                        return False
                    else: root = root.children[c]
                else:
                    found = False
                    for child in root.children:
                        found |= aux(word[i+1:], root.children[child])
                        if found:
                            return True
                    return found
            return root.end
        return aux(word, self.root)
    

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)