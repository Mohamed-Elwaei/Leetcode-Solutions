"""
i < j makes things difficult.


Solution might be a trie.
We will use a prefix trie, and a suffix trie.
We store a pair of characters for each node. The ith character in a string and the ith character from the end of a string
"""


class Node():
    def __init__(self):
        self.children = {}
        self.count = 0

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        trie = Node()
        ans = 0
        for word in words:
            root = trie
            for p in zip(word,word[::-1]):
                if p not in root.children:
                    root.children[p] = Node()
                ans += root.count
                root = root.children[p]
                
            ans += root.count
            root.count += 1
            
                    
        
        return ans