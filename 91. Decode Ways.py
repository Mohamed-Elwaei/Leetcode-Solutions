class Solution:
    def numDecodings(self, s: str) -> int:
        letters = {str(i + 1) : l for i,l in enumerate(string.ascii_lowercase)}
        memo = {}
        def dfs(curr, i):
            if (curr, i) in memo:
                return memo[(curr, i)]
            if curr not in letters:
                memo[(curr,i)] = 0
                return memo[(curr,i)]
            if i >= len(s):
                memo[(curr,i)] = 1
                return memo[(curr, i)]
                                #2 digit                1 digit
            memo[(curr,i)] = dfs(curr + s[i], i + 1) + dfs(s[i], i + 1)
            return memo[(curr,i)]
        return dfs(s[0], 1)