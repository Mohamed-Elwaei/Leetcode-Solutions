"""
prices. = [4,3,2,1]

We have n * (n+1) // 2 subarrays in an array.
then the answer will be 4*5/2 = 10 

[1], [2], [3], [4]
[4,3], [3,2], [2,1]
[4,3,2], [3,2,1]
[4,3,2,1]

Let's say we have an entire array of size n which has a smooth descent period.
Then each subarray in that array also has a smooth descent period.

The solution would be partition the array into subarrays that have a smooth descent period.
Then use the formula above for each subarray.
"""


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        
        curr = 1

        n = len(prices)
        answer = 0
        for i in range(1, n):
            if prices[i] == prices[i-1] - 1:
                curr += 1
            else:
                answer += curr * (curr + 1) // 2
                curr = 1
        answer += curr * (curr + 1) // 2
        return answer