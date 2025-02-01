class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=set(nums)
        if len(nums)<3:return max(nums)
        for i in range(0,2):
            nums.remove(max(nums))
        return max(nums)