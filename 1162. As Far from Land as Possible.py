from collections import deque
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        # 1 <= N <= 100
        #Each cell is 0 for water or 1 for land.
        N = len(grid)

        mat = [[-1] * N for _ in range(N)]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        queue = deque([])
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    queue.append((r,c))
                    mat[r][c] = 0

        if not queue or len(queue) == N*N:
            return -1


        while queue:
            row, col = queue.popleft()
            for deltaRow, deltaCol in directions:
                nextRow, nextCol = row + deltaRow, col + deltaCol
                if 0 <= nextRow < N and 0 <= nextCol < N and mat[nextRow][nextCol] == -1:
                    mat[nextRow][nextCol] = mat[row][col] + 1
                    queue.append((nextRow,nextCol))
        
        answer = 0
        for r in range(N):
            for c in range(N):
                answer = max(mat[r][c], answer)
        return answer