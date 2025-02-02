class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        #Only flip a row if the row has a leading 0. This is the optimal choice
        #Only flip a column if the column has more zeroes than ones.


        # row = [0,1,1,1,1,1,1,1]
        # row = [1,0,0,0,0,0,0,0]
        ROWS,COLS = len(grid),len(grid[0])
        for r in range(ROWS): 
            if grid[r][0] == 1: continue
            for c in range(COLS):
                grid[r][c] = 1 if grid[r][c] == 0 else 0
        for c in range(COLS): 
            zeroes = 0
            for r in range(ROWS):#O(m)
                zeroes += grid[r][c] == 0
            if zeroes <= ROWS // 2: 
                continue
            for r in range(ROWS):
                grid[r][c] = 1 if grid[r][c] == 0 else 0

        result = 0
        for row in grid:
            exponent = 0
            while row:
                result += row.pop() * (2 ** exponent)
                exponent += 1

        return result