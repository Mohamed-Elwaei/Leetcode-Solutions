class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l,r = matrix[0][0], matrix[-1][-1]

        while l <= r:
            mid = l + (r - l) // 2
            count = 0
            for row in matrix:
                for num in row:
                    count += int(num <= mid)
            if count >= k:
                r = mid - 1
            else:
                l = mid + 1
        return l
        