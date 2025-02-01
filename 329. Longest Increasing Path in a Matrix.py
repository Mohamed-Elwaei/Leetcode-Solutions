from collections import defaultdict
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows,cols = len(matrix),len(matrix[0])
        memo = defaultdict(lambda : 1)
        
        def bfs(r,c):
            if (r,c) in memo:
                return memo[(r,c)]
            directions = [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]
            visited.add((r,c))
           
            for nr,nc in directions:
                if (0<=nr<rows) and (0<=nc<cols) and matrix[nr][nc] > matrix[r][c] and matrix[r][c] not in visited:

                    memo[(r,c)] = max(memo[(r,c)], bfs(nr,nc) + 1)
            return memo[(r,c)]
        ans = 1
        for r in range(rows):
            for c in range(cols):
                visited = set()
                memo[(r,c)] = bfs(r,c)
                ans = max(memo[(r,c)],ans)
        return ans