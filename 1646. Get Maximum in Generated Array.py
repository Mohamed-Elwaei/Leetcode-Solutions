class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:return n
        nums=[0]*(n+1)
        nums[1]=1
        for i in range(1,len(nums)):
            if 2*i<len(nums):
                nums[2*i]=nums[i]
            if (2*i)+1<len(nums):
                nums[(2*i)+1]=nums[i]+nums[i+1]
        return max(nums)
    