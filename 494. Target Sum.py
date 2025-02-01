class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if not (-total <= target <= total):
            return 0
        dp = []
        for _ in range(len(nums)+1):
            dp.append([0] * (total - (-total) + 1))
        
        for i in range(len(dp[0])):
            dp[0][i] = int((i-total) == 0)
        
        for r in range(1,len(nums) + 1):
            for c in range(len(dp[0])):
                if 0<= c - nums[r-1] < len(dp[0]):
                    dp[r][c] += dp[r-1][c - nums[r-1]]
                if 0<= c + nums[r-1] < len(dp[0]):
                    dp[r][c] += dp[r-1][c + nums[r-1]]
        for row in dp:
            print(row)
        return dp[-1][target + total]