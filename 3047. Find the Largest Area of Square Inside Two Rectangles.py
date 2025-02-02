"""
Brute force: Loop over every pair of rectangles.
"""

class Solution:
    def largestSquareArea(self, A: List[List[int]], B: List[List[int]]) -> int:
        n = len(A)
        
        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                
                a = [max(A[i][0],A[j][0]), max(A[i][1],A[j][1])]
                b = [min(B[i][0],B[j][0]), min(B[i][1],B[j][1])]                
                
                side = min(b[0] - a[0], b[1] - a[1])
                
                if side > 0:
                    ans = max(side*side, ans)
        return ans