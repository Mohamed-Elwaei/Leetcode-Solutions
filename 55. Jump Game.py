"""
If we know we can reach nums[j] from nums[i] where j > i.

Then we know we can reach nums[i+1], nums[i+2], ... nums[j-1]

From nums[i] we want to reach index k such that nums[k] + k is maximised for all k in [i,i+nums[i]]

How do we find k efficiently for all i.

nums = [3,2,1,0,4]

tmp  = [4,3,2,1,0]


nums = [2,3,1,1,4]


dp = [2,max(1+3,2) = 4, max(1+2,4),max(1+3,4)]

tmp. = [4,3,2,1,0]
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        farthest = nums[0]
        n = len(nums)
        i = 0
        while i <= farthest and i < n - 1:
            farthest = max(nums[i] + i, farthest)
            i += 1
        return farthest >= n - 1
            