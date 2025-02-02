

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #If current letters match: Skip over both
        #Else: we branch

        """
        LCS(a,b) = {
            1 + LCS(a[1:],b[1:]), If letters match
            max(LCS(a[1:],b),LCS(a,b[1:])) If letters don't match
        }
        """
        memo = dict()
        def LCS(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i>=len(text1) or j>=len(text2):
                memo[(i,j)] = 0
            elif text1[i]==text2[j]:
                memo[(i,j)] = 1 + LCS(i+1,j+1)
            else:
                memo[(i,j)] = max(LCS(i+1,j),LCS(i,j+1))
            return memo[(i,j)]
        return LCS(0,0)