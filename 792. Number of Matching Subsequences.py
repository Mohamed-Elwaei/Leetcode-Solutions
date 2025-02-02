class Node:
    def __init__(self):
        self.children = {c:None for c in 'abcdefghijklmnopqrstuvwxyz'}
        self.end = False
class Trie:
    def __init__(self):
        self.root = Node()
    def insert(self,word):
        curr = self.root
        for letter in word:
            if curr.children[letter] == None:
                curr.children[letter] = Node()
            curr = curr.children[letter]
        curr.end = True

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        lookup = {c:[] for c in 'abcdefghijklmnopqrstuvwxyz'}
        for i,c in enumerate(s):
            lookup[c].append(i)
        
        def bs(index, lst):
            l,r = 0, len(lst) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if lst[mid] > index:
                    r = mid - 1
                else:
                    l = mid + 1
            return l
        matches = 0
        for word in words:
            index = -1
            found = True
            for letter in word:
                tmp = bs(index, lookup[letter])
                if tmp == len(lookup[letter]):
                    found = False
                    break
                else:
                    index = lookup[letter][tmp]
            matches += found
        return matches