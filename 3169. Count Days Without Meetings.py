"""
days = 10, meetings = [[5,7],[1,3],[9,10]]

days = 10, meetings = [[1,3],[5,7],[9,10]]

merge the overlapping intervals.

Then subtract all their sizes from days.
"""


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
    
        overlapped = []
        
        s,e = meetings[0]
        
        for m in meetings[1:]:
            
            if m[0] > e:
                overlapped.append([s,e])
                s,e = m
            else:
                e = max(e,m[1])
        
        overlapped.append([s,e])
        for s,e in overlapped:
            days -= (e - s + 1)
        return days