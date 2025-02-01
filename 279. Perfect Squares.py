class Solution:
    def numSquares(self, n: int) -> int:
        i = 1
        powers = []
        while i*i <=n:
            powers.append(i*i)
            i+=1
        matrix = []

        for power in powers:
            matrix.append([i for i in range(0,n+1)])
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                matrix[r][c] = matrix[r-1][c]
                if c - powers[r] >= 0:
                    matrix[r][c] = min(matrix[r][c - powers[r]] + 1, matrix[r][c])
        return matrix[-1][-1]