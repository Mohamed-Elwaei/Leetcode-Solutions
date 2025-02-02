class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        """
        nums = [2,5,6,8,5], k = 4
        sorted = [2,5,5,6,8]
        [2,4,5,6,8]
        [2,4,4,6,8]
        
        nums = [2,5,6,8,5], k = 7
        soered = [2,5,5,6,7] k = 7
        [2,5,6,6,7]
        [2,5,6,7,7]
        [2,5,7,7,7]
        
        soered = [2,5,5,6,7,19] k = 7
        If k > median, only increase numbers less than median on the right half
        If k < median, only decrease numbers more than the median on the left half.
        """
        
        nums.sort()
        N = len(nums)
        median = nums[N//2]
        operations = 0
        if median < k:
            for i in range(N//2, N):
                if nums[i] >= k: break
                operations += k - nums[i]
        elif median > k:
            for i in range(N//2,-1,-1):
                if nums[i] <= k:
                    break
                operations += nums[i] - k
        return operations
            