"""
Sort the rides array by increasing end time.

So let's say we pick up passenger i.
Then we get endi - starti + tipi.
And we can't get any passengers from starti+1 to endi.


So let DP[i] be the maximum profit at point i.

DP[i]'s optimal value will be.

max(endj - startj + tipj + DP[startj], DP[i-1]) for all rides[j] which have endj = i.

So by sorting at the beginning we gurantee that all DP[0], DP[1], ... DP[i-1] have already been computed.
"""

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        DP = [0] * (n+1)
        mapping = {end: [] for end in range(1,n+1)} #Map each endtime x to a all starti's and tipi's such that rides[i] = [starti, x, tipi]


        for start, end, tip in rides:
            mapping[end].append((start, tip))
        

        for end in range(1,n+1):
            DP[end] = DP[end-1]

            for start, tip in mapping[end]:
                profit = end - start + tip
                DP[end] = max(DP[end], DP[start] + profit)
    
        return DP[-1]