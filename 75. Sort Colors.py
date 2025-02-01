from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j=len(nums)
        vals={0:0,1:0,2:0}
        for i in ((nums)):
            vals[i]+=1
        for i in range(len(nums)):
            if vals[0]>0:
                nums[i]=0
                vals[0]-=1
                continue
            if vals[1]>0:
                nums[i]=1
                vals[1]-=1
                continue
            if vals[2]>0:
                nums[i]=2
                vals[2]-=1
                continue