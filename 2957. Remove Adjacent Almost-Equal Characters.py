class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        """
        Dimensions are the word we have.
        If the last character character is nearly equal, add 1 + min(last 2 characters)
        """
        def adj(a,b):
            return abs(ord(a) - ord(b)) <= 1
        
        N = len(word)
        dp = [0] * N
        
        for i in range(1, N):
            dp[i] = dp[i - 1]
            if adj(word[i - 1], word[i]):
                dp[i] = 1 + min(dp[i-1],dp[max(i-2,0)])
            
        return dp[-1]