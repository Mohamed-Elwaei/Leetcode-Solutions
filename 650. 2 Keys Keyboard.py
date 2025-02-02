class Solution:
    def minSteps(self, n: int) -> int:
        """
        Initially we have 1 A and 0 A's in our copy buffer.
        (A,C) initially A=1 and C=0.
        We don't want to paste if C=0 to not run into an infinite loop.
        We don't want to copy  if C=A to not run into an infinite loop.
        """

        memo = {}
        def dfs(A, C):
            if (A,C) in memo:
                return memo[A, C]
            if A == n:
                memo[A, C] = 0
                return memo[A, C]
            ans = float('inf')
            if C!=0 and A + C <= n:
                ans = 1 + dfs(A + C, C)
            if C!=A:
                ans = min(ans,1 + dfs(A,A))
            memo[A,C] = ans
            return memo[A,C]
        print(memo)
        dfs(1,0)
        return dfs(1,0)

            