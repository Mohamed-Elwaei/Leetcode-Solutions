import heapq
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        memo = dict()
        rows,cols = len(grid),len(grid[0])
        def dfs(row,c1,c2):
            if (row,c1,c2) in memo:
                return memo[(row,c1,c2)]
            elif row ==rows or min(c1,c2) < 0 or max(c1,c2) >= cols:
                memo[(row,c1,c2)] = 0
            elif c1==c2:
                memo[(row,c1,c2)] = 0
            elif row==rows-1:
                memo[(row,c1,c2)] = grid[row][c1] + grid[row][c2]
            else:
                memo[(row,c1,c2)] = grid[row][c1] + grid[row][c2] + max(
                    dfs(row+1,c1-1,c2-1), dfs(row+1,c1-1,c2),dfs(row+1,c1-1,c2+1),
                    dfs(row+1,c1,c2-1),   dfs(row+1,c1,c2), dfs(row+1,c1,c2+1),
                    dfs(row+1,c1+1,c2-1),   dfs(row+1,c1+1,c2), dfs(row+1,c1+1,c2+1)
                )
            return memo[(row,c1,c2)]
        dfs(row=0,c1=0,c2=cols-1)
        return memo[(0,0,cols-1)]
            
            