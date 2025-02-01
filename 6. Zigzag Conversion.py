class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        ROWS = numRows
        if ROWS == 1: return s
        matrix = [[''] * 1000 for r in range(ROWS)]
        r,c = 0,0
        direction = 0
        for i in range(len(s)):
            if direction == 0: #Down
                matrix[r][c] = s[i]
                if r < ROWS - 1: 
                    r += 1
                else:
                    r -= 1
                    c += 1
                    direction = 1
            elif direction == 1: #Up, to the right.
                matrix[r][c] = s[i]
                if r == 0:
                    direction = 0
                    r += 1
                else:
                    r = r - 1
                    c = c + 1
        ret = ''
        for row in matrix:
            ret += ''.join(row)
        return ret