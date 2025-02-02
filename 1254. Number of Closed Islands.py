"""
We will do a Breadth First Search.

We will map each cell with a 0 to a number. The number represents which connected component the cell is part of.

After doing the BFS, we will go through all border cells with value 0.
We will then assign the component those cells are a part of to be not-closed islands.
"""
from collections import deque
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        def bfs(r,c,color):
            nonlocal n,m
            queue = deque([(r,c)])
            while queue:
                r,c = queue.popleft()

                mapping[r,c] = color

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 0 and ((nr,nc) not in mapping):
                        queue.append((nr,nc))



        count = 0

        n,m = len(grid), len(grid[0])
        mapping = {} 
        nonclosed_islands = set()

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 0 and (r,c) not in mapping:
                    count += 1
                    bfs(r,c,count)
                if (r == 0 or c == 0 or r == n - 1 or c == m - 1) and ((r,c) in mapping):
                    nonclosed_islands.add(mapping[r,c])
        


        
        return count - len(nonclosed_islands)


