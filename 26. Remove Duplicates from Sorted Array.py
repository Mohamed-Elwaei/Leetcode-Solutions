from collections import defaultdict
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash=defaultdict(lambda:-1)
        i=0
        while i<len(nums):
            if hash[nums[i]]==-1:
                hash[nums[i]]=i
            else:
                del nums[i]
                continue
            i+=1    
        return len(nums) 