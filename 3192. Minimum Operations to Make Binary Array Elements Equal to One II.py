"""

Consider nums[i].

Let zeroes and ones be arrays of size n.

zeroes[i] is minimum flips it takes to make nums[i...n-1] = 0.
ones[i] is minimum flips it takes to make nums[i...n-1] = 1.


What is the minimum flips to make nums[i..n-1] == 1 and to make nums[i..n-1] == 0.

We have 2 choices:

If nums[i] == 1:
    Consider how many flips to make nums[i+1 .. n-1] = 1.

If nums[i] == 0:
    Consider how many flips to make nums[i+1 .. n-1] = 0.


"""

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        zeroes = 0
        ones = 0
        if nums[-1] == 0:
            ones = 1

        elif nums[-1] == 1:
            zeroes = 1


        for i in range(n-2,-1,-1):

            if nums[i] == 0:
                ones = zeroes + 1
            elif nums[i] == 1:
                zeroes = ones + 1

        return ones