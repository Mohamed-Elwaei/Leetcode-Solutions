"""
4!

We get the longest decreasing subarray ending at nums[n-1]

Let's say that subarray starts at index i. 

If i = 0. return the array sorted.

If i > 0. We check the no. at nums[i-1].

We check the smallest number with index j in nums[i .. n-1] such that i <= j <= n-1 and nums[j] > nums[i].

We swap nums[j] and nums[i-1].

We sort nums[i..n-1]
= 

[1,2,3,4]
[1,2,4,3]
[1,3,2,4]
[1,3,4,2]
[1,4,2,3]
[1,4,3,2]

[2,1,3,4]
[2,1,4,3]
[2,3,1,4]
[2,3,4,1]
[2,4,1,3]
[2,4,3,1]

[3,1,2,4]
[3,1,4,2]
[3,2,1,4]
[3,2,4,1]
[3,4,1,2]
[3,4,2,1]

[4,1,2,3]
[4,1,3,2]
[4,2,1,3]
[4,2,3,1]
[4,3,1,2]
[4,3,2,1]



nums = [1,1,5]

[1,5,1]
[5,1,1]
[1,1,5]
"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #First get the index i such that nums[i...n-1] is monotonically decreasing.
        n = len(nums)
        i = n - 1
        
        # Find the longest decreasing suffix
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        
        # If the entire array is non-increasing, reverse it to get the smallest permutation
        if i == 0:
            nums.reverse()
            return
        
        # Find the rightmost element that exceeds nums[i - 1]
        j = n - 1
        while nums[j] <= nums[i - 1]:
            j -= 1
        
        # Swap the found element with nums[i - 1]
        nums[i - 1], nums[j] = nums[j], nums[i - 1]
        
        # Reverse the suffix to get the next permutation
        nums[i:] = reversed(nums[i:])