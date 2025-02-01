class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) //2
            if nums[mid] > nums[-1]:
                l = mid + 1
            elif nums[mid] < nums[-1]:
                r = mid - 1
            elif nums[mid] == nums[-1]:
                break
        print(f'Min element {nums[mid]} in index {mid}')
        if nums[-1] >= target: l,r = mid, len(nums) - 1
        elif nums[0] <= target: l,r = 0, mid
        while l <= r:
            mid = l + (r - l) //2
            if nums[mid] == target: return mid
            elif nums[mid] > target: r = mid - 1
            elif nums[mid] < target: l = mid + 1
        return -1 
        