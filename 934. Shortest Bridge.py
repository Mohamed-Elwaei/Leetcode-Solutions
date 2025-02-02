from collections import deque

directions = [[1,0],[-1,0],[0,1],[0,-1]]
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        def dfs(r,c,island):
            stack = [(r,c)]

            while stack:
                r,c = stack.pop()
                island.add((r,c))

                for dr,dc in directions:
                    nr = dr + r
                    nc = dc + c

                    if 0 <= nr < n and 0 <= nc < n and (nr,nc) not in island and grid[nr][nc] == 1:
                        stack.append((nr,nc))
            

        island1 = set()
        island2 = set()

        n = len(grid)
        for row in grid:
            print(row)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    if (i,j) not in island1 and len(island1) == 0:
                        dfs(i,j,island1)
                    elif (i,j) not in island2:
                        dfs(i,j,island2)

        

        queue = deque([[r,c,0] for r,c in island1])
        visited = {(r,c) for r,c in island1}
        answer = 0
        while queue:
            r,c,dist = queue.popleft()



            for dr,dc in directions:
                nr = dr + r
                nc = dc + c

                if 0 <= nr < n and 0 <= nc < n:
                    if (nr,nc) in island1 or (nr,nc) in visited: 
                        continue
                    if (nr,nc) in island2: 
                        return dist

                    visited.add((nr,nc))
                    queue.append((nr,nc, dist + 1))
        