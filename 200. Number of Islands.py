from collections import deque

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows,cols=len(grid),len(grid[0])
        count=0
        def DFS(i,j):
            if 0<=i<rows and 0<=j<cols and grid[i][j]=='1':
                grid[i][j] = '#'
                DFS(i+1,j)
                DFS(i-1,j)
                DFS(i,j+1)
                DFS(i,j-1)
            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    DFS(i,j)
                    count+=1
        return count