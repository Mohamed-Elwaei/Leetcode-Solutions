class Solution:
    def __init__(self):
        self.ways = 0
    def climbStairs(self, n: int) -> int:
        memo = dict()
        memo[0] = 0
        memo[2] = 2
        memo[1] = 1

        def dfs(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = dfs(n-1) + dfs(n-2)
                return memo[n]
        return dfs(n)