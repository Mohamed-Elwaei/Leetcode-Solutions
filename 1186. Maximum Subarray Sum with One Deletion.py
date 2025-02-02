"""
Only consider negative numbers for deletion.

So for each nums[i].
Consider the maximum subarray including nums[i].
The maximum subarray including nums[i] can be found with a prefix sum and a suffix sum.

Let PS and SS be two arrays of size n.

Let PS[i] be the maximum subarray ending at index i.
Let SS[i] be the maximum subarray starting at index i.

The maximum subarray with nums[i] = PS[i] + SS[i] - nums[i].
We would consider deleting nums[i].

"""

class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        PS = [0] * n #Let PS[i] be the maximum subarray ending at index i.
        SS = [0] * n #Let SS[i] be the maximum subarray starting at index i.
        
        curr = 0
        min_ = 0
        for i in range(n):
            curr += arr[i]
            PS[i] = curr - min_
            min_ = min(curr,min_)
        
        curr = 0
        min_ = 0
        for i in range(n-1,-1,-1):
            curr += arr[i]
            SS[i] = curr - min_
            min_ = min(curr,min_)


        answer = min(arr)
        for i in range(n):
            maxSubarray = PS[i] + SS[i] - arr[i]
            maxSubarrayWithRemoval = maxSubarray - arr[i]
            if PS[i] + SS[i] == arr[i] * 2:
                answer = max(answer, maxSubarray)
            else:
                answer = max(answer, maxSubarray, maxSubarrayWithRemoval)
        
        return answer