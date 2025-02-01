def minimumTotal( triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp=[[float('inf')] * len(n) for n in triangle]

        def dfs(curr,total):
            r,c=curr
            if r == len(triangle) - 1:
                dp[r][c] = triangle[r][c]
                return dp[r][c]

            if dp[r][c] != float('inf'):
                return dp[r][c]

            directions=[(r+1,c),(r+1,c+1)]

            for d in directions:
                a,b = d
                if a<len(triangle) and b<len(triangle[a]):
                    dp[r][c]=min(dp[r][c],dfs(d,total+triangle[r][c])+triangle[r][c])
            return dp[r][c]
        dfs((0,0),0)
        return dp[0][0]

triangle=[[2],[3,4],[6,5,7],[4,1,8,3]]

print(minimumTotal(triangle))