"""
Anything multiplied by 0 is 0. We don't want 0 in our subarray.
negative * negative is negative. We want an even number of negative integers in our subarray.

We can partition the array into subarrays that have no 0's and 1 0. Ignore the subarrays with one 0.

Example:
nums = [-1,-2,-3,0,1]
we would partition this into [-1,-2,-3] and [1] and then solve a similar problem without 0's.


If we had a negative array and we wanted to 'shrink it', we can't shrink it because we might run into another negative number.
But if we wanted to shrink it, we would remove the earliest negative number.


Suppose that arr[i ... j] is negative. That means we have an odd number of negative numbers.
We should remove the earliest occuring negative number which will then give us an even number of negative numbers, and a positive product subarray.

Suppose that arr[i ... j] is negative. 
Find the smallest k such that i <= k <= j and arr[j] < 0. That means the longest subarray ending at j has length j - k + 1.
"""


def F(nums): #F returns the maximum length of a subarray with positive product assuming nums has no 0's.

    last = -1
    parity = 0
    n = len(nums)
    answer = 0
    for r in range(n):
        if nums[r] < 0:
            parity ^= 1
            if last == -1:
                last = r
        
        if parity == 1:
            answer = max(answer, r - last)
        else:
            answer = max(answer, r+1)
    return answer

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:

        left = 0
        n = len(nums)
        answer = 0
        for right in range(n):
            if nums[right] == 0:
                answer = max(answer, F(nums[left: right]))
                left = right + 1

        if left < n:
            answer = max(answer, F(nums[left:]))
        return answer
