def minCut( s: str) -> int:
        matrix = [[None] * (len(s) + 1) for _ in range(len(s) * 1)]
        palindrome = [[None] * (len(s) + 1) for _ in range(len(s) * 1)]

        
        for i in range(len(s)):
            matrix[i][i+1] = 0
            matrix[i][i] = 0
            palindrome[i][i+1] = 1
            palindrome[i][i] = 1

    
        for k in range(len(s)):
            for i in range(len(s)-k ):
                if matrix[i][k+i+1]:
                    continue
                if s[i:k+i+1][0] == s[i:k+i+1][-1] and palindrome[i][k+i]:
                    palindrome[i][k+i] = 1
                    matrix[i][k+i+1] = 0
                else:
                    matrix[i][k+i+1] = float('inf')
                    for j in range(i+1,k+i+1):
                      matrix[i][k+i+1] = min(1 + matrix[i][j] + matrix[j][k+i+1] ,matrix[i][k+i+1])
    
        return matrix[0][len(s)]



print(minCut("efe"))

        