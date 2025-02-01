class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        matrix = []
        for _ in coins + [0]:
            matrix.append([float('inf')] * (amount + 1))
        
        matrix[0][0] = 0
        rows,cols = len(matrix),len(matrix[0])
        for r in range(1,rows):
            for c in range(cols):
                if 0 <= c - coins[r-1]:
                    matrix[r][c] = min(matrix[r-1][c], matrix[r][c - coins[r-1]] + 1)
                else:
                    matrix[r][c] = matrix[r-1][c]

        return matrix[-1][-1] if matrix[-1][-1]!=float('inf') else -1