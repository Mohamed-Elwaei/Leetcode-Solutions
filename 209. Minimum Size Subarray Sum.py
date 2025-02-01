class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        ans = float('inf')

        l,r = 0,0

        ans = float('inf')

        l,r = 0,0

        curr = 0
        while r<len(nums):

            while r<len(nums) and curr<target:
                curr+=nums[r]
                r+=1

            while l<=r and curr>=target:
                
                ans = min(ans,r - l)
                curr-=nums[l]
                l+=1
        
        if ans == float('inf'): 
            return 0
        return ans
