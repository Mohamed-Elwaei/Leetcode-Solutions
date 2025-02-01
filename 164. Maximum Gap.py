class Solution(object):
    def  counting_sort(self,nums,exp):
        output=len(nums)*[0]
        count=10*[0]
        for i in nums:
            idx=(i//exp)%10
            count[idx]+=1
        for i in range(1,10):
            count[i]+=count[i-1]
        for i in nums[::-1]:
            idx=(i//exp)%10
            output[count[idx]-1]=i
            count[idx]-=1
        for i in range(len(output)):
            nums[i]=output[i]

    def radix_sort(self,nums):
        max_num=max(nums)
        exp=1
        while max_num//exp>0:
            self.counting_sort(nums,exp)
            exp*=10
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.radix_sort(nums)
        maxdiff=0
        for i in range(1,len(nums)):
            maxdiff=max(maxdiff,nums[i]-nums[i-1])
        return maxdiff