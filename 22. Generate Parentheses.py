class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        curr = ''
        ways = []
        def dfs(open, closed):
            nonlocal curr
            if closed > open or open > n or closed > n:
                return
            if open == closed and closed == n:
                ways.append(curr[:])
                return
            
            curr += '('
            dfs(open + 1, closed)
            curr = curr[:-1]

            curr += ')'
            dfs(open, closed + 1)
            curr = curr[:-1]
        dfs(0,0)
        return ways