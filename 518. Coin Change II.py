class Solution:
    def change(self, amount: int, coins: List[int]) -> int: 
        matrix = []
        for _ in coins + [0]:
            matrix.append([1] + [0] * (amount))
        matrix[0][0] = 1

        rows,cols = len(matrix), len(matrix[0])

        for r in range(1,rows):
            for c in range(1,cols):
                
                if c - coins[r-1] < 1:
                    matrix[r][c] = matrix[r-1][c]
                else:
                    tmp = c 
                    while tmp >= 1:
                        matrix[r][c] += matrix[r-1][tmp]
                        tmp-=coins[r-1]
                matrix[r][c]+= int(c % coins[r-1] == 0)
        # for r in matrix:
        #     print(r)
        return matrix[-1][-1]