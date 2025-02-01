class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = set()
        for i in range(len(nums)):
            val = abs(nums[i])
            idx = val - 1
            if nums[idx] < 0:
                duplicates.add(val)
            else:
                nums[idx] *= -1
        return list(duplicates)
            