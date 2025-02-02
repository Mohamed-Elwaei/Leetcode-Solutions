"""
let DP be an array of size n.

DP[i] = maximum earnings generated from the first i houses.
by default DP[i] = DP[i-1].


for each i in [0,n-1]:
    DP[i] = DP[i-1]

    for all offers i with end i:
        DP[i] = max(DP[i], gold i + DP[start - 1])

n 
m = len(offers)

memory complexity: O(n + m)
TIme complexity: O(n+m)
"""

class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        
        mapping = {i:[] for i in range(n)} #maps each end i to all offers that have end i.

        for start, end, gold in offers:
            mapping[end].append((start, gold))
        
        DP = [0] * n #DP[i] is the maximum profit from the first i houses.

        for end in range(n):
            if end > 0:
                DP[end] = DP[end-1]

            for start, gold in mapping[end]:
                if start > 0:
                    DP[end] = max(DP[end], gold + DP[start-1])
                else:
                    DP[end] = max(DP[end], gold)
        return DP[n-1]