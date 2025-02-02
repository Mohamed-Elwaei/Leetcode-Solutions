"""
Since the square is centered at the origin, it has to have an even length.

A square with side length 2n has corners: [n,n],[n,-n],[-n,n],[-n,-n].

So a point [x,y] will lie on a sqaure with sidelength max(2x,2y).

First, sort the array by the magnitude of the points, and see how many points can be fit in.

points = [[2,2],[-1,-2],[-4,4],[-3,1],[3,-3]], s = "abdca"


After sorting...

{b,a}
points = [([-1,-2],[2,2]),([-3,1],[3,-3]),([-4,4])], s = "(ba)(ca)d"


points = [[1,1],[-1,-1],[2,-2]], s = "ccd"
 
after sorting...

 points = [([1,1],[-1,-1]),([2,-2])], s = "(cc)d"


"""
from collections import defaultdict
class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        
        H = defaultdict(list) #Key: Integer => list of labels of points which have max(x,y) = Key.
        
        for (x,y),label in zip(points,s):
            
            key = max(abs(x),abs(y))
            H[key].append(label)
            
        H = sorted(list(H.items()))
        
        S = set()
        print(H)
        
        for _, labels in H:
            
            tmp = set(labels)
            
            if len(tmp) != len(labels):
                break
            
            flag = 0
            for l in labels:
                if l in S:
                    flag = 1
                    break
            if flag == 1:
                break
            
            for l in labels:
                S.add(l)
        return len(S)
        
        