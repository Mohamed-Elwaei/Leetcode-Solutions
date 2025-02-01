class Solution:
    def isInterleave(self, s: str, t: str, p: str) -> bool:
        """
        At the last letter of s3, the last letter of s1 or s2 must match.
        Then we trim s3 by 1 (s3 == s3[:-1]).
        We can then either trim s1, or s2 by one. So we have 2 choices.

        First make sure the length of s1, and s2 sum up to the length of s3.
        If s3[-1] == s2[-1] == s1[-1]. return F(s3[-1], s2[-1],s1) or F(s3[-1],s2, s1[-1])
        elif s3[-1] == s2[-1]: return F(s3[:-1])
        """
        if len(s) + len(t) != len(p):
            return False

        memo = {}

        def dfs(i,j):
            k = i + j
            if i == len(s) and j == len(t):
                return True
            elif (i,j) in memo:
                return memo[i,j]
            elif i >= len(s):
                memo[i,j] = t[j:] == p[k:] 
            elif j >= len(t):
                memo[i,j] = s[i:] == p[k:]
            elif s[i] == p[k] and t[j] == p[k]:
                memo[i,j] = dfs(i + 1, j) or dfs(i, j + 1)
            elif s[i] == p[k]:
                memo[i,j] = dfs(i + 1, j)
            elif t[j] == p[k]:
                memo[i,j] = dfs(i, j + 1)
            else:
                memo[i,j] = False
            return memo[i,j]
        return dfs(0,0)