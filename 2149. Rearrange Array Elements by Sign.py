class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        copy = [0] * len(nums)
        p,n = 0, len(nums)//2
        for i in range(len(nums)):
            if nums[i] > 0:
                copy[p] = nums[i]
                p+=1
            else:
                copy[n] = nums[i]
                n+=1
        print(copy)
        p,n = 0,len(nums)//2
        i = 0
        while i<len(nums):
            nums[i] = copy[p]
            nums[i+1] = copy[n]
            i,p,n = i+2,p+1,n+1
        return nums