class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        for r in range(n-2,-1,-1):
            for c in range(n):
                smallest = float('inf')
                for k in range(n):
                    if k!=c:
                        smallest = min(smallest, grid[r+1][k])
                grid[r][c]+=smallest
        return min(grid[0])
            
        