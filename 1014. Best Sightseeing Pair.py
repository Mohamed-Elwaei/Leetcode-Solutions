"""
If values[i] > values[j] and i > j, we can discard j.

If values[i] < abs(i - j) for all j > i, we can discard values[i]

values = [8,1,5,2,6]
For example we are never going to be pairing index 4 with 1 because nums[1] < abs(4 - 1)
6 + 1 - 3.

The solution would be using a prefix sum of some sort.


let PS be an array of size n.

PS[i] = max(nums[i], PS[i-1] - 1).

For each i in range [0,n]:
    consider the best pair that has index i.
    find the optimal nums[j] such that values[j] + i - j is maximized.
    the optimal nums[j] for i will be stored in PS[i].
    Solution would be PS[i] + nums[i]
"""

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)

        #PS[i] will contain the maximum answer for values[j] + i - j.
        # PS = [0] * n

        #DP[i] will contain the maximum sightseeing pair with index i.
        # DP = [0] * n


        # PS[0] = values[0]
        PS = values[0]
        DP = 0
        answer = 0
        for i in range(1,n):
            DP = PS - 1 + values[i]
            PS = max(values[i], PS - 1)
            answer = max(answer, DP)
        
        return answer