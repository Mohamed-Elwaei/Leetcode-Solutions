class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=sorted(nums)
        l=0
        r=len(nums)-1
        currmax=0
        while l<r:
            currmax=nums[l]+nums[r] if nums[l]+nums[r]>currmax else currmax
            l+=1
            r-=1
        return currmax