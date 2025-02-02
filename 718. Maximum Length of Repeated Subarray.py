class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        #Bottom Up approach:
        #Base case: one of the arrays is empty. Then the answer is 0.
        rows, cols = len(nums1), len(nums2)

        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        #We will go right to left, bottom to up.

        for r in range(rows - 1,-1,-1):
            for c in range(cols - 1,-1,-1):
                if nums1[r] == nums2[c]:
                    dp[r][c] = 1 + dp[r+1][c+1]
        longest = 0
        for row in dp:
            longest = max(longest, max(row))
        return longest