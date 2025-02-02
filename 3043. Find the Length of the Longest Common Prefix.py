"""
Brute force approach is O(n^2).

I think we could use a trie.

Convert all numbers in arr2 into strings.
Store each string in a trie.

Trie to search for the longest common prefix.

For each num in arr1:
    Calculate how deep down the trie we can go.
The answer will be the maximum depth for all nums in arr1.
"""

def insert(word, trie): #Inserts word into a trie.
    
    root = trie
    for c in word:
        if c not in root:
            root[c] = dict()
        root = root[c]

        
def depth(word, trie): #Calculate the maximum depth that word can go inside the trie.
    root = trie
    D = 0
    
    for c in word:
        if c not in root:
            break
        
        else:
            D += 1
            root = root[c]
    return D

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = {}
        
        arr2 = [str(x) for x in arr2]
        
        
        
        for word in arr2:
            insert(word, trie)
        
        
        arr1 = [str(x) for x in arr1]
        
        ans = 0
        
        for word in arr1:
            ans = max(ans, depth(word, trie))
            
        return ans
        