"""
If we had 3 cells c1,c2,c3 with values a,b,c.

Moving from c1 to c2 to c3 = (b - a) + (c - b) = c - a
Moving from c1 to c3  = c - a.
2 choices,
grid = [
    [9,5,7,3],
    [8,9,6,1],
    [6,7,14,3],
    [2,5,3,1]
    ]

dp = [
    [INF,5,5,3],
    [8,5,5,1],
    [6,5,5,3],
    [2,5,3,1]
    ]

"""

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        dp = []

        for row in grid:
            dp.append(row[:])
        n,m = len(dp), len(dp[0])

        for i in range(1,m):
            dp[0][i] = min(grid[0][i-1], dp[0][i-1])
        for i in range(1,n):
            dp[i][0] = min(grid[i-1][0], dp[i-1][0])

        
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1],grid[i-1][j],grid[i][j-1])
        
        ans = float('-inf')
        dp[0][0] = float('inf')

        for row in dp:
            print(row)
        
        for i in range(n):
            for j in range(m):
                ans = max(ans, grid[i][j] - dp[i][j])
        return ans