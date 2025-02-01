class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = 0
        n = len(citations)
        l,r = 0, len(citations) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if citations[mid] < n - mid:
                l = mid + 1
            else:
                r = mid - 1
        if citations[mid] == 0:
             return 0
        return n - l
            