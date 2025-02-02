"""
2-D Dynammic Programming problem.

the dimensions would be arr and k.

DP = array the same size as arr.

DP[i] = largest sum of arr[0..i] after partitioning.

arr = [1,15,7,9,2,5,10], k = 3
ans = [15,15,15,9,10,10,10]

DP = [1,max(15 + 1, 15*2) = 30, max(30 + 7, 15*2 + 1, 15*3) = 45, max(9 + 45, 9*2 + 30, 15*3 + 1) = 54,

max(2 + 54, 9*2 + 45, 9*3 + 1) = 63, max(5 + 63, 5*2 + 54, 9*3 + 45) = 68, max(10 + 68, 10*2 + 63, 10*3 + 54) = 84
]

return value will be DP[n-1].
"""

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        DP = [0] * n
        DP[0] = arr[0]

        for j in range(1,n):

            M = arr[j]
            for i in range(j,max(-1,j-k),-1):
                M = max(arr[i], M)

                if i == 0:
                    DP[j] = max(DP[j], M *(j - i + 1))
                else:
                    DP[j] = max(DP[j], M*(j - i + 1) + DP[i-1])

        #Time complexity is O(n*k).
        #Memory complexity is O(n).
        return DP[-1]