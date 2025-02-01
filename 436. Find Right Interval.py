class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        copy = sorted(intervals)
        lookup = {tuple(interval):index for index,interval in enumerate(intervals)}
        def bs(interval):
            l,r = 0, len(copy) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if copy[mid][0] >= interval[1]:
                    r = mid - 1
                else:
                    l = mid + 1
            if l >= len(copy): return -1
            return lookup[tuple(copy[l])]
        
        ans = []
        for interval in intervals:
            ans.append(bs(interval))
        return ans