class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        ans = [0]
        def dfs(score,power, l, r):
            if l > r:
                ans[0] = max(ans[0],score)
                return
            if tokens[l] <= power:
                dfs(score + 1, power - tokens[l], l + 1, r)
            elif score > 0:
                dfs(score - 1, power + tokens[r], l , r - 1)
            ans[0] = max(ans[0],score)
        dfs(0,power,0,len(tokens) - 1)
        return ans[0]