class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memo = dict()
        M = [10**9 + 7]
        def dfs(r,c,moves):
            if moves == 0:
                return int((not (0 <= r < m) or not (0<=c < n)))
            elif (r,c,moves) in memo:
                return memo[(r,c,moves)] % M[0]
            elif not (0 <= r < m) or not (0<=c < n):
                memo[(r,c,moves)] = 1
                return memo[(r,c,moves)]
            else:
                memo[(r,c,moves)] = (dfs(r+1,c,moves-1) + dfs(r-1,c,moves-1) + dfs(r,c+1,moves-1) + dfs(r,c-1,moves-1)) % M[0]
                return memo[(r,c,moves)]
        return dfs(startRow, startColumn, maxMove)