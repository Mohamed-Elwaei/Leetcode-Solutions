class Node:
    def __init__(self,val):
        self.val = val
        self.children = dict()
        self.end = False
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
        return 
def search(word,count,root):
        curr = root
        for i,c in enumerate(word):
            if c not in curr.children:
                return False
            else:
                curr = curr.children[c]
                if curr.end and search(word[i+1:],count+1,root):
                    return count+1
        if curr.end:
            return count
                    


class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        words = sorted(words,key = lambda x: len(x))
        trie = Trie()

        conc = []
        for word in words:
            trie.insert(word)
        for word in words:
            res = search(word,1,trie.root)
            if res>=2:
                conc.append(word)
        return conc


words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
sol = Solution()
print(sol.findAllConcatenatedWordsInADict(words))
        