class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows,cols=len(grid),len(grid[0])
        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c] in ['#',0]:
                return
            
            grid[r][c]='#'
            area[0]+=1

            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        
        maxArea=0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area=[0]
                    dfs(r,c)
                    maxArea=max(maxArea, area[0])
        
        return maxArea