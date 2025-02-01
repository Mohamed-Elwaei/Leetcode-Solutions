class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if mid - 1 < 0 or mid + 1 >= n or nums[mid - 1] < nums[mid] < nums[mid + 1]:
                return nums[mid]
            elif (nums[mid] == nums[mid - 1] and (n - mid) % 2 == 1) or (nums[mid] == nums[mid + 1] and (n - mid) % 2 == 0) :
                r = mid - 1
            else:
                l = mid + 1
        return nums[l]