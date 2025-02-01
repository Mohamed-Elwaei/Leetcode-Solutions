class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        nums=sorted(nums)
        n=len(nums)
        curr=0
        majorities=set()
        last=None

        for num in nums:
            if num==last:
                curr+=1
            else:
                curr=1
                last = num
            
            if curr>n//3:
                majorities.add(last)
        return majorities
            
            