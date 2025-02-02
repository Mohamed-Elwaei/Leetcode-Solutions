"""
Let m <= n be the amount of 0's in the array.

So we have to choose 1 out of m positions.

Let's record the largest amount to the left and right of each 0. and decide which 0 to delete.
nums = [0,1,1,1,0,1,1,0,1]
left =  [0,3,2]
right = [3,2,1].

The answer will be max(left[i] + right[i] for each i)

nums = [0,1,1,1,0,0,1,1,0,1]
left =  [0,3,0,2]
right = [3,0,2,1]

"""

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = []
        right = []

        count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                left.append(count)
                count = 0
            else:
                count += 1
        count = 0
        for i in range(n-1,-1,-1):
            if nums[i] == 0:
                right.append(count)
                count = 0
            else:
                count += 1
        
        right = right[::-1]

        answer = 0
        for i in range(len(left)):
            answer = max(answer, left[i] + right[i])

        return max(count - 1 ,answer)