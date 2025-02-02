class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N = len(word1)
        M = len(word2)

        #Given two strings word1 and word2, 
        #return the minimum number of steps required to make word1 and word2 the same.
        #In one step, you can delete exactly one character in either string.
        # 1 <= M, N <= 500.

        #Step 1: find the Longest Common Subsequence (LCS). 
        #Step 2: remove all elements from both words that are not in LCS.
        memo = {}
        def LCS(i,j):
            if i >= N or j >= M:
                return 0
            if (i,j) in memo:
                return memo[i,j]
            elif word1[i] == word2[j]:
                memo[i,j] = 1 + LCS(i + 1, j + 1)
            else:
                memo[i,j] = max(LCS(i + 1, j),LCS(i, j + 1))
            return memo[i,j]
        
        LCS = LCS(0,0)
        return N + M - (2 * LCS)
        