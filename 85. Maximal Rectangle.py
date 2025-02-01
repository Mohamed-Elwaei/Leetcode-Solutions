"""
matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]

dp = [
    [1,0,1,0,0],
    [1,0,3,2,1],
    [5,4,3,2,1],
    [1,0,0,1,0]
]

Calculate for each cell. what is the biggest rectangle that the cell is an upper right corner of?

First let's count the amount of consecutive 1's at each cell to the right.


If this is a matrix with n rows and m columns,

this solution would take O(n * m) extra memory and it would take O(n*m *n) time complexity.
"""

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n,m = len(matrix), len(matrix[0])

        for i in range(n):
            for j in range(m):
                matrix[i][j] = int(matrix[i][j])

        for row in matrix:
            for i in range(m-2,-1,-1):
                if row[i] != 0:
                    row[i] += row[i+1]
        answer = 0
        
        for i in range(n):
            for j in range(m):
                horizontal = matrix[i][j]
                for k in range(i,n):
                    horizontal = min(horizontal, matrix[k][j])
                    vertical = k - i + 1
                    answer = max(answer, vertical * horizontal)
        return answer