class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()

        i = 0
        ans = []
        while i < len(intervals):
            j = i+1
            merged = [intervals[i][0],intervals[i][1]]
            while j < len(intervals) and merged[0]<=intervals[j][0]<=merged[1]:
                merged[1] = max(intervals[j][1],merged[1])
                j+=1
            i = j
            ans.append(merged)
        return ans