class Solution(object):
    def counting_sort(self,nums,exp):
        output=[0]*len(nums)
        count=[0]*10
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
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        nums=[int(x) for x in nums]
        self.radix_sort(nums)
        print(nums)
        return str(nums[-k])