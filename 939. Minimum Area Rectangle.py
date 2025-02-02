"""
One thing to notice is that in a rectangle with points [x1,y1],[x2,y2],[x3,y3],[x4,y4].


We can pair the points such that x1 == x2 and x3 == x4, y1 == y2 and y3 == y4.


points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]

points are [3,1],[3,3],[4,1],[4,3].


We can solve this in O(n^2).

for (x1,y1) in points:
    for (x2,y2) in points:

        3 cases:
        if x1 == x2:
            then y1 and y2 are different.
            So find the smallest x such that [x,y1] and [x,y2] are points
        if y1 == y2:
            then x1 and x2 are different.
            So find the smallest y such that [x1,y] and [x2,y] are points
        if neither is true:
            then both points are at opposite corners.
            So find 2 points with coordinates [x2,y1] and [x1,y2]
        
"""



class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        S = set((x,y) for x,y in points)
        n = len(points)
        answer = float('inf')
        for i in range(n):
            for j in range(i+1,n):
                x1,y1 = points[i]
                x2,y2 = points[j]

                if x1 != x2 and y1 != y2 and ((x1,y2) in S) and ((x2,y1) in S):
                    answer = min(answer, abs(y2 - y1) * abs(x2 - x1))
        
        if answer == float('inf'):
            answer = 0

        return answer