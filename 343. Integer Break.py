class Solution:
    def integerBreak(self, n: int) -> int:
        matrix = []
        for _ in range(n+1):
            matrix.append([0] * (n+1))
        
        for i in range(2,n+1):
            for j in range(1,i):
                matrix[i][j] = (j * (max(matrix[i - j] + [i-j])))
        # for r in matrix:
        #     print(r)
        return max(matrix[-1])