class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr_max = Max = nums[0]

        for i in range(1,len(nums)):
            curr_max = max(nums[i],nums[i] + curr_max)
            Max = max(curr_max, Max)
        return Max