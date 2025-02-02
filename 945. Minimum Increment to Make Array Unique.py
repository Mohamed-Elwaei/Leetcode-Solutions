"""
nums = [3,2,1,2,1,7]
nums = [1,1,2,2,3,7]


nums = [1,2,3,4,5,7]

operations = 6


sort the array.

for each number in the array:
    if the previous number is more than or equal to the current number:
        increment the current number by (previous number - current number + 1)

"""

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        operations = 0
        n = len(nums)
        for i in range(1,n):
            # print(nums)
            if nums[i-1] >= nums[i]:
                operations += (nums[i-1] - nums[i] + 1)
                nums[i] += (nums[i-1] - nums[i] + 1)
        return operations