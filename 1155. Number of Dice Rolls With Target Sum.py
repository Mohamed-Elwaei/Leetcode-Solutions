class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if target > (n*k):
            return 0
        ways = [0] * ((k*n)+1)
        ret = [0] * ((k*n)+1)
        for i in range(1,k+1):
            ways[i] = 1
        
        for n_ in range(0,n):
            ret = ways[:]
            for i in range(len(ways)):
                ways[i] = (sum(ret[max(0, i - k):i])  ) % (10**9 + 7)
            
        return ret[target]
            