from collections import deque
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        currSum = sum(nums[0:k])
        avg = float('-inf')

        l,r = 0,k

        while r<len(nums):
            avg = max(avg,currSum/float(k))
            currSum-=nums[l]
            currSum+=nums[r]
            l+=1
            r+=1
        avg = max(avg,currSum/float(k))
        return avg