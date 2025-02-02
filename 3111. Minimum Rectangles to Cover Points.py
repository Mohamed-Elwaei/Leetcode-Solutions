"""
Each rectangle has its lower end at some point (x1, 0) and its upper end at some point (x2, y2), where x1 <= x2, y2 >= 0, and the condition x2 - x1 <= w must be satisfied for each rectangle.

y2 can be anything. We can make our rectangle as high as possible. We do not need to pay attention to the y axis.
We can just project all the points on the x axis.

Example:

points = [[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]], w = 2

points = [0,1,2,3,4,5,6]


"""

class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        
        points = [x for x,y in points]
        points.sort()
        
        
        end = -1
        
        count = 0
        for p in points:
            if p > end:
                end = p + w
                count += 1
        
        return count
                
        
        
        