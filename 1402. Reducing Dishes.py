"""
Include a negative satisfaction[i] if it leads to a bigger time[i]
for the positive satisfaction[i] in the future.


The larger the number, the bigger time[i] it should have.
The smaller the number, the smaller time[i] it should have.

First sort the array.
let DP be a two dimensional matrix.

DP[i][j] = optimal array with size i not necessarily ending at index j.

DP[i][j] = max(DP[i-1][0] DP[i-1][1]... DP[i-1][j-1]) + i * nums[j].

answer is maximum cell in DP.

"""

class Solution:
    def maxSatisfaction(self, A: List[int]) -> int:
        
        A.sort()


        ans = 0
        sum = 0

        for n in A[::-1]:
            
            if ans + sum + n > ans:
                ans = ans + sum + n
                sum += n
        
        return ans