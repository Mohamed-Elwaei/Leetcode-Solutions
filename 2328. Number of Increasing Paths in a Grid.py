"""
We will have a 2D matrix 'DP' initially set to all 1's.
DP[i][j] will have the count of how many strictly increasing paths end at grid[i][j] in the original grid.


DP[i][j] += sum of neighbours where neighbours have a less value

grid = 
[
    [1,1],
    [3,4]
]

DP = 
[
    [1,1],
    [2,4]
]

Problem is the order in which we start. Start with the smallest cells first.
"""

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:

        rows,cols = len(grid),len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        M = int(1e9 + 7)
        DP = [[1] * cols for _ in range(rows)]

        order = []
        for r in range(rows):
            for c in range(cols):
                order.append((r,c))
        order.sort(key = lambda x: grid[x[0]][x[1]])
        
        print(order)
        for r,c in order:
            for dr,dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > grid[r][c]:
                    DP[nr][nc] = (DP[nr][nc] + DP[r][c]) % M
        
        sum = 0
        for row in DP:
            for cell in row:
                sum = (sum + cell) % M
        return sum

