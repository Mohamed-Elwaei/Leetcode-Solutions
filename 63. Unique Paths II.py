class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #We Can only move down or right.
        #We should cache revisited states to avoid recomputation and wasting time or resources.
        #Oue base case is at the bottom right cell where there is only one path.
        #If we are in a cell that has an obstaccle, that cell has 0 paths.
        grid = obstacleGrid
        rows,cols = len(grid), len(grid[0])
        memo = {(rows - 1, cols - 1): 1 if grid[-1][-1] == 0 else 0}

        def dfs(r,c):
            if (r,c) in memo:
                return memo[(r,c)]
            elif r >= rows or c >= cols:
                return 0
            elif grid[r][c] == 1:
                memo[(r,c)] = 0
            else:
                memo[(r,c)] = dfs(r + 1,c) + dfs(r, c + 1)
            return memo[(r,c)]
        return dfs(0,0)