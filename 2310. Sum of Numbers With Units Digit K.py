
class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        DP = [float('inf')] * (num + 1)
        DP[0] = 0
        for i in range(1, num + 1):
            
            
            for j in range(1, i+1):
                if str(k) != str(j)[-1]: continue
                DP[i] = min(DP[i], 1 + DP[i - j])
        if DP[num] == float('inf'):
            return -1
        return DP[num]