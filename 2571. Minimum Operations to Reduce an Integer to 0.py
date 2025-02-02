"""
n = 39
32 + 4 + 2 + 1

10 0111


n = 40
32 + 8
10 1000


Base case is if n is a power of 2. We require one operation/
If n is 0, no operations are required.


n = 54 = 32 + 16 + 4 + 2

11 0110

11 1000

100 0000.


n = 15

1111
1 0000
0 0000


We want to iterate in the reverse order.

For each n in [1,max_n] descending:
    for each bit i:
        DP[n] = min(DP[n], DP[n + (1 << i)])
"""

def bitCount(n):
    bits = 0
    while n:
        n = n & (n-1)
        bits += 1
    return bits

max_n = int(1e5 + 1)
DP = [bitCount(i) for i in range(max_n)]



for n in range(max_n-1,-1,-1):

    for i in range(17):
        if n + (1 << i) < max_n:
            DP[n] = min(DP[n], 1 + DP[n + (1 << i)])



class Solution:
    def minOperations(self, n: int) -> int:

        return DP[n]
        