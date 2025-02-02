class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        """
        If subarray sum is < m, it is invalid unless it's length is one
        
        for [2,3,3] to be valid either [2] and [3,3] must be or [2,3] and [3]
        [2,3] is invalid.
        
        for [2,3,3,2,3] to be valid, one of the following must be valid:
        [2,3,3,2] and [3]
        [2,3,3] and [2,3]
        [2,3] and [3,2,3]
        [2] and [3,3,2,3]
        
        for [2,3,3,2] to be valid, one of the following must be valid:
        [2,3,3] and [2]
        [2,3] and [3,2]
        [2] and [3,3,2]
        """
        memo = {}
        def dfs(l, r, total):
            
            if (l,r) in memo:
                return memo[l, r]
            elif r - l == 1:
                memo[l,r] = 1
            elif total < m:
                memo[l,r] = False
            else:
                memo[l,r] = 0
                tmp = nums[l]
                for mid in range(l+1,r):
                    memo[l,r] = memo[l,r] | (dfs(l,mid, tmp) & dfs(mid,r,total - tmp))
                    tmp += nums[mid]
            return memo[l,r] 
        if len(nums) <= 2:
            return True
        return dfs(0, len(nums), sum(nums))