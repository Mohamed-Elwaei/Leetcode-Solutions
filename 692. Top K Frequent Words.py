class Node:
    def __init__(self):
        self.children = {s:None for s in 'abcdefghijklmnopqrstuvwxyz'}
        self.end = self.count = 0
class Trie:
    def __init__(self):
        self.root = Node()
    def insert(self,word):
        curr = self.root
        for c in word:
            if curr.children[c] == None:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.end = True
        curr.count += 1
        
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        heap = []
        def dfs(curr, word):
            if curr.end:
                heapq.heappush(heap, (-curr.count, word))
            for letter,child in curr.children.items():
                if child != None:
                    dfs(curr.children[letter], word + letter)
        dfs(trie.root, '')
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans
            