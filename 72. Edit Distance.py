class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        T,P = len(word1),len(word2)

        dp = []

        for _ in range(P+1):
            dp.append([None] * (T+1))
        for i in range(P+1):
            dp[i][0] = i
        for i in range(T+1):
            dp[0][i] = i
        
        for i in range(1,P+1):
            for j in range(1,T+1):
                if word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
        return dp[P][T]