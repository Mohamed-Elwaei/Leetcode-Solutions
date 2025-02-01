import heapq
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        heap = []

        for i,n in enumerate(nums):
            heapq.heappush(heap, (n,i))
        
        nums = []
        while heap:
            nums.append(heapq.heappop(heap))
        
        for i in range(1,len(nums)):
            if nums[i][0] == nums[i-1][0] and abs(nums[i][1] - nums[i-1][1]) <=k:
                return True
        return False
        