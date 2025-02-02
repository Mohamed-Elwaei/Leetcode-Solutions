"""
We would use a hasmap first.
We would map each point to the number of times it occurs.

the function add is simple to increment.

But how do we increment count?


If we have a point (x1,y1), and we want to count how many squares it's in,

Then we'll loop over the points.

for each (x2,y2) in points:
    there are 3 cases;

    First case is if x1 == x2:
        the points are on the same vertical side.
        So we have to find 2 neighbouring points with the same x's but different y's

    Second case is if y1 == y2:
        the points are on the same horizontal side.
        So we have to find 2 neighbouring points with the same y's but different x's

    Third case is if x1 != x2 and y1 != y2:
        we find 2 points. One with (x1,y2) and the other with (x2,y1).
        If we find those 4 points, we multiply their occurences.

"""

from collections import defaultdict

class DetectSquares:

    def __init__(self):
        self.P = {}

    def add(self, point: List[int]) -> None:
        P = self.P
        point = tuple(point)
        P[point] = P.get(point, 0) + 1
  

    def count(self, point: List[int]) -> int:
        x1,y1 = point
        P = self.P
        answer = 0

        for x2,y2 in P.keys():
            if abs(x2 - x1) == abs(y2 - y1) and x2 != x1 and y2 != y1 and (x1, y2) in P and (x2, y1) in P:
                answer +=  P[x2, y2] * P[x1, y2] * P[x2, y1]
        return answer

        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)