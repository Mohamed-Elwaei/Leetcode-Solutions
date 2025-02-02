class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(pos, gold, ans):
            r, c = pos
            tmp = grid[r][c]
            gold += tmp
            grid[r][c] = 0
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > 0:
                    dfs((nr, nc), gold, ans)
            grid[r][c] = tmp
            ans[0] = max(ans[0], gold)

        rows, cols = len(grid), len(grid[0])
        ans = [0]  # Using a list to pass by reference
        for r in range(rows):
            for c in range(cols):
                dfs((r, c), 0, ans)
        return ans[0]