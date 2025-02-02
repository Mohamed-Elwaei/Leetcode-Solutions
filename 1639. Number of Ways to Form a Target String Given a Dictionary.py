"""
Let dp be a 2D array.
Let aux be a 2D array.


aux[i][c] = no. of words which have letter c in their ith character.
aux will be a (words[0].length x 26) matrix


dp[i][j] = no. of ways to form the prefix target[0 .. i] in target using the first j letters in each word.

If j < i: 
    dp[i][j] = 0

by default dp[i][j] = dp[i][j-1]

dp[i][j] = dp[i][j - 1] + (dp[i-1][j-1] * aux[i][target[j]])


(dp[i-1][j-1] * aux[i][target[j]]) 

dp[i-1][j-1] = no. of ways to form prefix target[0 .. i-1] using the j - 1 characters in each word.
aux[i][target[j]] = no. of words with character target[j] in their ith position.

multiplying these two yields the no. of ways to form prefix target[0 .. i] using the first j letters in each word

"""
M = int(1e9 + 7)

class Solution(object):
    def numWays(self, words, target):
        """
        :type words: List[str]
        :type target: str
        :rtype: int
        """
        """
        :type words: List[str]
        :type target: str
        :rtype: int
        """
        aux = []
        n = len(words[0])
        m = len(words)
        p = len(target)
       
        for _ in range(n):
            aux.append({c:0 for c in string.ascii_lowercase})
   

        for i in range(m):
            for j in range(n):
                c = words[i][j]
                aux[j][c] += 1
        
        dp = []

        for _ in range(p):
            dp.append([0] * n)


        dp[0][0] = aux[0][target[0]]
        for j in range(1,n):
            c = target[0]
            dp[0][j] = (aux[j][target[0]] + dp[0][j-1]) % M
  
        
        for i in range(1, p):
            for j in range(i,n):
                dp[i][j] = (dp[i][j - 1] + (aux[j][target[i]] * dp[i-1][j-1]) % M) % M
        return dp[-1][-1]