"""
We have n choices to drop the first egg.

If we choose and index x to drop the first egg. There are two branches or two possible outcomes,

If the first egg breaks:
    We drop the second from 1 to x-1.
    It takes at most 1 + (x-1) drops.

If it does not break:
    We drop the second from x+1 to n-1.
    It takes at most 1 + (n-1 - x+1 + 1) = 1 + (n - x + 1).


If we have input n.

If we decide to drop the egg at x where 1 <= x <= n.
Then if the first egg breaks:
    We have to check [1,x-1] x-1 - 1 + 1
If the first egg does not break:
    We have to [x+1,n] n - (x+1) + 1

for mid in [1,n]:
    if we drop the first egg at mid

    dp[i] = min(dp[i], 1 + max(dp[mid-1], dp[n - mid + 1 + 1]))

"""

max_n = 1001  # Considering floors from 0 to 1000
DP = [float('inf')] * max_n
DP[1] = 1
DP[0] = 0

for n in range(2, max_n):
    for x in range(1, n + 1):  # x should range from 1 to n
        DP[n] = min(DP[n], 1 + max(x-1, DP[n - x]))


class Solution:
    def twoEggDrop(self, n: int) -> int:
        print(DP[:n+1])
        return DP[n]
        