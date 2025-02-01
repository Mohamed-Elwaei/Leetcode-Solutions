class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=0
        zeroes=0
        while n<len(nums)-zeroes:
            if nums[n]==0:
                del nums[n]
                nums.append(0)
                zeroes+=1
                continue
            n+=1
        