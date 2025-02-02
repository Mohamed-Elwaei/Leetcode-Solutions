class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        matrix = []
        for _ in range(366):
            matrix.append([None] * 3)
        for i in range(3):
            matrix[0][i] = 0
        for r in range(1,366):
            if r not in days:
                matrix[r] = matrix[r-1][:]
                continue
            for c in range(3):
                if c==0:
                    matrix[r][c] = min(matrix[r-1]) + costs[0]
                if c==1:
                    matrix[r][c] = min(min(matrix[max(r-7,0)]) +  costs[1] ,matrix[r][c-1])
                if c==2:
                    matrix[r][c] = min(min(matrix[max(r-30,0)]) +  costs[2],matrix[r][c-1])

        return min(matrix[days[-1]])
                

                    