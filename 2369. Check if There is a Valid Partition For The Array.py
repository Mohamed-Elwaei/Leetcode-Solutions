"""
This looks like a regular DP problem.

Let DP be a boolean array of size n.

DP[i] will be true if there is a valid partition for nums[0...i].



for each i in [0,n]:
    DP[i] = False
    if i > 0 and nums[i-1] == nums[i]:
        DP[i] = DP[i] or (i == 1 or DP[i-2]).
    
    if i > 1 and nums[i-2] == nums[i-1] == nums[i]:
        DP[i] = DP[i] or (i == 2 or DP[i-3])
    
    if i > 1 and nums[i-2] + 2 == nums[i-1] + 1 == nums[i]:
        DP[i] = DP[i] or (i == 2 or DP[i-3])
        
"""

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        

        DP = 0
        DP_1 = 0
        DP_2 = 0
        DP_3 = 0
        for i in range(n):
            DP = False
            
            if i > 0 and nums[i-1] == nums[i]:#Condition 1
                DP = DP or i == 1 or DP_2
            
            if i > 1 and nums[i-2] == nums[i-1] and nums[i-1] == nums[i]:#Condition 2
                DP = DP or i == 2 or DP_3
            
            if i > 1 and nums[i-2] + 2 == nums[i-1] + 1 and  nums[i-1] + 1 == nums[i]:#Condition 3
                DP = DP or i == 2 or DP_3
            
            DP_3, DP_2, DP_1 = DP_2, DP_1, DP
        return DP