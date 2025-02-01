class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows,cols=len(board),len(board[0])
        visited=set()
        def dfs(r,c,i):
            
            if i==len(word):
                return True
            if (r>=rows or r<=-1 or
                 c>=cols or c<=-1 or
                 (r,c) in visited or word[i]!=board[r][c]):
                return False
            
            
            visited.add((r,c))

            left,right,up,down=dfs(r,c-1,i+1),dfs(r,c+1,i+1),dfs(r-1,c,i+1),dfs(r+1,c,i+1)
            visited.remove((r,c))
            if sum([left,right,up,down]):
                return True
            return False
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r,c,0):
                    return True
        return False