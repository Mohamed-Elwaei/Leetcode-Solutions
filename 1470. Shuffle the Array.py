class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        ans=[]
        for i in range(len(nums)/2):
            ans.append(nums[i])
            ans.append(nums[i+(len(nums)/2)])
        return ans