from collections import deque


directions = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        n,m = len(grid), len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    grid[i][j] = -1
                if grid[i][j] == 0:
                    grid[i][j] = -2
        
        #Now the grid has all unvisited cells 
        queue = deque([(0,0)])
        grid[0][0] = 1
        while queue:
            r,c = queue.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == -2:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr,nc))
        

        if grid[n-1][m-1] == -2:
            return -1 #No clear path
        return grid[n-1][m-1]
        
