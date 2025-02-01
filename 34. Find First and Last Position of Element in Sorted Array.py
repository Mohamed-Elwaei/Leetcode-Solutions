class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return -1,-1
        l,r = 0, len(nums) - 1
        first = last = -1
        while l<=r:
            mid = l + (r - l) // 2
            if nums[mid] >= target:
                first = mid
                r = mid - 1
            else:
                l = mid + 1
        l,r = 0,len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] <= target:
                last = mid
                l = mid + 1
            else:
                r = mid - 1
        if nums[first] == target: return first,last
        return -1,-1