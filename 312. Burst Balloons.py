from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]  # Add 1 before and after the nums array
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        
        for length in range(2, n):
            for left in range(0, n - length):
                right = left + length
                for k in range(left + 1, right):
                    dp[left][right] = max(dp[left][right],
                                          nums[left] * nums[k] * nums[right] +
                                          dp[left][k] + dp[k][right])
        
        return dp[0][n - 1]
