class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums)==1:
            return nums[0]
        return max(self.Rob(nums[1:],len(nums)-2,memo=dict()),
        self.Rob(nums,len(nums)-2,memo=dict()))

    def Rob(self,nums,i,memo):
        if i<0:
            return 0
        if i in memo:
            return memo[i]

        result=max(self.Rob(nums,i-2,memo)+nums[i] ,self.Rob(nums,i-1,memo))
        
        memo[i] = result

        return memo[i]
       