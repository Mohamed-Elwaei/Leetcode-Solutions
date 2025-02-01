"""
If we could reuse the elements, we could just add 1 to the array.

n should be equal to the sum of nums at least.
Smallest number in nums should be 1.
The array nums is sorted.

If nums[i] != nums[i+1] - 1, then we need to insert a new number.


nums = [1,5,10], n = 20

[1,5] we need to insert 2.
[1,2,5]
[1,2,4,5]
"""

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        N = len(nums)

        index = upto = output = 0
        while upto < n:
            if index < N and nums[index] <= upto + 1:
                upto += nums[index]
                index += 1
            else:
                upto += (upto + 1)
                output += 1
        return output