class Node:
    def __init__(self, val,children=None):
        self.val = val
        self.children = children or {}
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
        curr.end=True
            

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        trie = Trie()

        for w in wordDict:
            trie.insert(w)
        
        ans,sent = [],[]
        def dfs(i=0,curr='',root=trie.root):
            if i ==len(s) :
                if root.end:
                    ans.append(sent[:] + [curr])
                    return
                else:
                    return
            if root.end:
                sent.append(curr)
                dfs(i, '', trie.root)
                sent.pop()

            curr += s[i]
            if curr[-1] not in root.children:
                return 
            else:
                dfs(i+1, curr ,root.children[curr[-1]])
        dfs()
        for i,sentence in enumerate(ans):
            ans[i] = ' '.join(sentence)
        
        return ans