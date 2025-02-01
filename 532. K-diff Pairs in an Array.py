class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        def bs(num, l, r):
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] - num > k:
                    r = mid - 1
                elif nums[mid] - num < k:
                    l = mid + 1
                else:
                    return mid
            return float('inf')

        count = 0
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums) and nums[j] == nums[i]: 
                j += 1
            pair = (i, bs(nums[i],i + 1, len(nums) - 1))
            if pair[-1] != float('inf'):
                count += 1
            i = j
        return count
        