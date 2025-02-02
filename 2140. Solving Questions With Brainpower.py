"""
let DP be an array of size n.

Let DP[i] be the maximum points for solving questions 0 to i.

DP[i] = max(DP[i+1], points[i] + DP[i + brainpower[i]]).

The iteration order will be in reverse to acheive this effect.
"""

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        DP = [0] * n
        DP[n-1] = questions[n-1][0]

        for i in range(n-2,-1,-1):
            if i + questions[i][1] < n-1:
                DP[i] = max(DP[i+1], questions[i][0] + DP[i + questions[i][1] + 1])
            else:
                DP[i] = max(DP[i+1], questions[i][0])

        
        return DP[0]