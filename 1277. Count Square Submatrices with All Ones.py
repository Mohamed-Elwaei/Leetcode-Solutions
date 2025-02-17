class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # 1 <= rows <= 300
        # 1 <= cols <= 300
        #arr[i][j] is either 1 or 0
        #We want to return the number of squares
        #If we have an n*n square, then we have sum((i^2) (n - i + 1)^2) for i from 0 to n.
        #We also don't want to recount any squares.

        #If we have a 4 * 4 square, then we have 
        #1 4 * 4 square. n^2
        #4 3 * 3 squares.
        #9 2 * 2 squares
        #16 1 * 1 squares.

        memo = {}
        rows, cols = len(matrix), len(matrix[0])
        def dfs(r,c):
            if (r,c) in memo:
                return memo[(r,c)]
            elif r >= rows or c >= cols: 
                return 0
            elif matrix[r][c] == 1:
                memo[(r,c)] = min(dfs(r + 1, c) ,dfs(r, c + 1),dfs(r + 1, c + 1)) + 1
            else:
                memo[(r,c)] = 0
            return memo[(r,c)]
            
        answer = 0
        for r in range(rows):
            for c in range(cols):
                answer += dfs(r,c)
        return answer