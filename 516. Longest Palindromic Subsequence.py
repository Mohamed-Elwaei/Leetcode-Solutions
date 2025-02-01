class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = dict()
        memo[''] = 0
        def dfs(s):
            if s in memo:
                return memo[s]
            if not s:
                memo[s] = 0
                return memo[s]

            if len(s) == 1:
                memo[s] = 1
                return 1
            
            if s[0] == s[-1]:
                memo[s] = 2 + dfs(s[1:-1])
                return memo[s]
            else:
                memo[s] = max(dfs(s[1:]),dfs(s[:-1]))
                return memo[s]

        return dfs(s)

        