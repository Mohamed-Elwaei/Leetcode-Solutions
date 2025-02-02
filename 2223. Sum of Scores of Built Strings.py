def z_algo(s):
    n,l,r = len(s), 0, 0
    z = [0] * n

    for i in range(1,n):
        if i< r:
            z[i] = min(r - i, z[i - l])
        
        while i + z[i] < n and s[z[i]] == s[z[i] + i]:
            z[i] +=1
        
        if i + z[i] > r:
            l = i
            r = i + z[i]
        
    return z

class Solution:
    def sumScores(self, s: str) -> int:

        return sum(z_algo(s)) + len(s)
        