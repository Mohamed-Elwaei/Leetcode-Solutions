class Node:
    def __init__(self):
        self.children = dict()
        self.end = False
class Trie:
    def __init__(self):
        self.root = Node()
    def insert(self,word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c] 
        curr.end = True
    
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        def dfs(curr ,path ,pos):
            r,c = pos
            letter = path[-1]
            if letter not in curr.children: return
            else: curr = curr.children[letter]
            
            visited.add(pos)
            if curr.end:
                answer.add(''.join(path))

            for nr,nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited:
                    next = board[nr][nc]
                    dfs(curr,path + [next], (nr,nc))
            visited.remove(pos)

        rows,cols = len(board),len(board[0])
        answer = set()
        for r in range(rows):
            for c in range(cols):
                visited = set()
                dfs(trie.root,[board[r][c]],(r,c))
        return answer
        