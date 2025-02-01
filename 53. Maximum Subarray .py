def maxSubArray(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=nums[0]
        for r in range(len(nums)):
            l=r

            while l > -1 and sum(nums[:l]) >0:
                ans=max(ans,sum(nums[l:r]))
                l-=1
        return ans


nums=[-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))