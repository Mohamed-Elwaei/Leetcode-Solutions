class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2: # If odd return False
            return False
        half = total//2
        rows,cols = len(nums)+1, half + 1
        dp = []
        for _ in range(rows):
            dp.append([0] * cols)
        
        for r in range(rows):
            dp[r][0] = 1
        
        for r in range(1,rows):
            for c in range(1,cols):
                dp[r][c] = dp[r-1][c] #Default: set next row as the one before it 
                if c - nums[r-1] >= 0:
                    dp[r][c]|=dp[r-1][c - nums[r-1]]
        return dp[-1][-1]

        #for row: 3 col: 5: can we pick elements from the first 3 elements in arr to sum up to 5
        # Memory & Time Complexity: length of nums * half of the sum

        