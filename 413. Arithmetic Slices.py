class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        subs = 0
        for i in range(len(nums)-1):
            j = i + 1
            k = j+1
            while k < len(nums) and nums[k] - nums[k-1] == nums[j] - nums[i]:
                subs+=1
                k+=1
        return subs