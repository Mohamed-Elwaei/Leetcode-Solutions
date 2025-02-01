class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            # mid = (r + l) // 2
            if nums[mid] <= nums[-1]:
                r = mid - 1
            else:
                l = mid + 1
        return nums[l]