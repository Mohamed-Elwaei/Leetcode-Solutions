class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        n = len(matrix)

        for r in range(n-2,-1,-1):
            for c in range(n):
                Next = [matrix[r+1][c],matrix[r+1][max(0,c-1)],matrix[r+1][min(n-1,c+1)]]
                matrix[r][c]+=min(Next)
        
        return min(matrix[0])