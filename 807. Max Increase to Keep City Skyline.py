class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rows = [max(row) for row in grid]
        cols = [0] * n
        for c in range(n):
            for r in range(n):
                cols[c] = max(cols[c], grid[r][c])
        count = 0
        for r in range(n):
            for c in range(n):
                count += min(rows[r],cols[c]) - grid[r][c]
        return count