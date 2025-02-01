class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []

        l = 0
        while l < len(intervals):
            start, end = intervals[l]
            r = l + 1
            while r < len(intervals) and intervals[r][0] <= end:
                end = max(end,intervals[r][1])
                r+=1
            merged.append([start, end])
            l = r
        return merged
            