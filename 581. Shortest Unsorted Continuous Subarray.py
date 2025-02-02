class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        copy = sorted(nums)
        l = 0
        while l < len(nums) and nums[l] == copy[l]:
            l += 1
        r = len(copy) - 1
        while r > l and nums[r] == copy[r]:
            r -= 1

        return r - l + 1