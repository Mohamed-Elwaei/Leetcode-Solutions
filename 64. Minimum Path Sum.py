def minPathSum( grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        rows,cols=len(grid) , len(grid[0])

        sumR = 0
        for r in range(rows-2,-1,-1):
            grid[r][-1] += grid[r+1][-1]
        
        for c in range(cols-2,-1,-1):
            grid[-1][c] += grid[-1][c+1]
        
        rows-=1
        cols-=1

        for r in range(rows-1,-1,-1):
            for c in range(cols-1,-1,-1):
                grid[r][c] = grid[r][c] + min(grid[r][c+1],grid[r+1][c])
        return grid[0][0]

grid = [[1,3,1],
        [1,5,1],
        [4,2,1]]
print(minPathSum(grid))
