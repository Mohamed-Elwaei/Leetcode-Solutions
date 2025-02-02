from collections import Counter
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        cache = {}
        def score(x):
            s = 0
            for c in x:
                s += ord(c)
            return s

        def LCS(i,j):
            if i >= len(s1) or j >= len(s2):
                return ''
            elif (i,j) in cache:
                return cache[i, j]
            cache[i,j] = max(LCS(i + 1, j), LCS(i, j + 1), key = score )
            if s1[i] == s2[j]:
                cache[i,j] = max(s1[i] + LCS(i+1, j + 1), cache[i,j], key = score)
            return cache[i,j]
        LCS(0,0)
        bestLCS = 0
        for LCS in cache.values():
            bestLCS = max(bestLCS, score(LCS))
        return score(s1) + score(s2) - 2 * bestLCS