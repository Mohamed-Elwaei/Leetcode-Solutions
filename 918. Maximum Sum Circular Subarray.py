"""
We have two cases:

Subarray wraps around the beginning.
Subarray does not wrap around the beginning.

Solution:
Check the maximum subarray that 'wraps around' and the maximum subarray that does not wrap around.

To check the maximum subarray that 'wraps around' we can use a prefix sum.

Let PS and SS both be an array of size n. let
PS[i] = largest sum subarray that starts from the beginning of arr[0 .. i].
SS[i] = sum of the subarray arr[i..n-1].

Maximum subarray that 'wraps around' will be 
max(SS[i] + PS[i-1]) for all i's.


The maximum subarray that does not wrap around is solvable with a sliding window.
"""

def maxSubarraySum(arr): #computes the maximum subarray sum that does not 'wrap around'.

    curr = 0
    answer = float('-inf')
    for n in arr:
        curr += n
        answer = max(curr, answer)
        if curr < 0:
            curr = 0
    
    return answer


def maxSubarrayCircular(arr): #computes the maximum subarray sum that may wrap around the array.

    n = len(arr) 
    PS = [0] * n

    curr = 0
    maxPrefixSum = 0
    for i in range(n):
        curr += arr[i]
        maxPrefixSum = max(maxPrefixSum, curr)
        PS[i] = maxPrefixSum
    
    suffixSum = 0
    answer = float('-inf')
    for i in range(n-1,0,-1):
        suffixSum += arr[i]
        answer = max(suffixSum + PS[i-1], answer)
    return answer


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        return max(maxSubarraySum(nums), maxSubarrayCircular(nums))