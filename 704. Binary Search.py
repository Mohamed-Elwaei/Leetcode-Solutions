class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        last = 0
        while l<=r:
            mid = l + (r - l) // 2
            if nums[mid] > target:
                r = mid - 1
            else:
                last = mid
                l = mid + 1
        
        return last if nums[last] == target else -1