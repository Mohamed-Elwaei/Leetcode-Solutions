class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        

        memo = []

        for _ in range(len(s)+1):
            memo.append([None] * (len(t)+1))

        def dfs(i,j):
            if j >=len(t):
                memo[i][j] = 1
                return memo[i][j]
            if i >=len(s):
                memo[i][j] = 0
            
            if memo[i][j]!=None:
                return memo[i][j]

            if s[i] == t[j]:
                memo[i][j] = dfs(i+1,j+1) + dfs(i+1,j)
                return memo[i][j]
            else:
                memo[i][j] = dfs(i+1,j)
                return memo[i][j]
        return dfs(0,0)