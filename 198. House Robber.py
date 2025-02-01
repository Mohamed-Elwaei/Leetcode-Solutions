"""
We have 2 choices at each house.

If we rob it we can't rob the next house.
If we don't rob it, we can rob the next house.


dp[i] = max(house i + dp[i-2], dp[i-1])
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        A = nums[0] #dp[i-1]
        B = 0 #dp[i-2]
        ans = A #dp[i]


        # for i in range(2, n+1):         
        #     dp[i] = max(dp[i-2] + nums[i-1], dp[i-1])

        for i in range(2,n+1):
            ans = max(B + nums[i-1], A)

            A, B = ans, A

        return ans