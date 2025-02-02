class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        memo = {(k,startPos):1}
        k = [k]
        startPos = [startPos]
        m = [10**9 + 7]

        def dfs(pos = endPos, curr = 0):
            if (pos,curr) in memo:
                return memo[(pos,curr)]
            if curr == k[0]:
                memo[(pos,curr)] = int(pos == startPos[0])
                return memo[(pos,curr)] 
            else:
                memo[(pos,curr)] = dfs(pos+1,curr+1) + dfs(pos-1,curr+1)
                return memo[(pos,curr)] % m[0]
        return dfs()
        