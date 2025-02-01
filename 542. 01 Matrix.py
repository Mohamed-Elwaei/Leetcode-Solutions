from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        dp = [row[:] for row in mat]
        rows, cols = len(mat), len(mat[0])
        for r in range(rows):
            for c in range(cols):
                dp[r][c] = -1
                if mat[r][c] == 0:
                    queue.append((r,c))
                    dp[r][c] = 0
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while queue:
            row, col = queue.popleft()
            for delta_row, delta_col in directions:
                nextRow, nextCol = row + delta_row, col + delta_col
                if 0 <= nextRow < rows and 0 <= nextCol < cols and dp[nextRow][nextCol] == -1:
                    dp[nextRow][nextCol] = 1 + dp[row][col]
                    queue.append((nextRow, nextCol))
        return dp

                