class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if n <= 3:
            return 0
        
        j = -1
        ans = float('inf')
        for i in range(3,-1,-1):
            ans = min(nums[j] - nums[i], ans)
            j-=1
        return ans