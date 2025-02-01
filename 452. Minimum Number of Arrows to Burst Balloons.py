class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        arrows = 0
        l = 0
        while l < len(points):
            r = l + 1
            start, end = points[l]
            while r < len(points):
                start = max(start, points[r][0])
                end = min(end, points[r][1])
                if start > end: break
                r += 1
            #r - l == Amount of balloons we can pop with a single arrow
            l = r
            arrows += 1
        return arrows