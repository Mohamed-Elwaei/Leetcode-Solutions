"""
We would have 4 auxillary nxn matrices with: left, right, downward upward.

left[r][c] = longest sequence of 1's starting at (r,c) and going left.
right[r][c] = longest sequence of 1's starting at (r,c) and going right.
downward[r][c] = longest sequence of 1's starting at (r,c) and going downward.
upward[r][c] = longest sequence of 1's starting at (r,c) and going upward.


for r in range(rows):
    for c in range(cols):
        DP[r][c] = longest plus sign centered at cell (r,c).

        DP[r][c] = min(left[r][c], right[r][c], downward[r][c], upwards[r][c]) - 1.

answer = max(DP[r][c] for all cells (r,c))
"""

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        left = []
        right = []
        downward = []
        upward = []


        for _ in range(n):
            left.append([1] * n)
            right.append([1] * n)
            downward.append([1] * n)
            upward.append([1] * n)
        for r,c in mines:
            left[r][c] = right[r][c] = downward[r][c] = upward[r][c] = 0
        

        for r in range(n):
            for c in range(1,n):
                if left[r][c]:
                    left[r][c] += left[r][c-1]
        for r in range(n):
            for c in range(n-2,-1,-1):
                if right[r][c]:
                    right[r][c] += right[r][c+1]
        for c in range(n):
            for r in range(1,n):
                if upward[r][c]:
                    upward[r][c] += upward[r-1][c]
        for c in range(n):
            for r in range(n-2,-1,-1):
                if downward[r][c]:
                    downward[r][c] += downward[r+1][c]
        

        answer = 0
        for r in range(n):
            for c in range(n):
                answer = max(answer, min(left[r][c],right[r][c],downward[r][c],upward[r][c]))
        for row in left:
            print(row)
        return answer