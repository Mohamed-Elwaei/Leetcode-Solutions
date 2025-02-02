"""
The solution here would be For each cell (r,c)
count how many submatrices (rectangles) have cell (r,c) as the top left corner.


So we only need to consider two corners: top left corner and the top right corner.
Then we would see how many rectangles have those two cells as their corners.
We can do this in O(m*n*n)

Let DP[r][c] be the longest downward sequence of 1's starting from cell (r,c).


Let's say we have two upper corners in a rectangle (r,c1) and (r,c2) with c1 <= c2.

The number of rectangles with those 2 points as the upper corners is min(DP[r][c1], DP[r][c1+1], ... ,DP[r][c2])
"""

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:

        rows,cols = len(mat), len(mat[0])

        for r in range(rows - 2, -1, -1):
            for c in range(cols - 1,-1,-1):
                if mat[r][c] == 1:
                    mat[r][c] = 1 + mat[r+1][c]
            
        

        answer = 0
        for r in range(rows):
            for c1 in range(cols):
                if mat[r][c1] == 0: continue
                height = mat[r][c1]


                for c2 in range(c1,cols):
                    if mat[r][c2] == 0: break
                    height = min(height, mat[r][c2])
                    answer += height
        return answer