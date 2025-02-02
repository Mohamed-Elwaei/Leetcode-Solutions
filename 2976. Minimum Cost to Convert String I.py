"""
Shortest path problem.
Let n = source.length.
n can be very large.

We have 26 letters in the alphabet.
We can calculate the shortest path for each pair of letters in O(26^3) using floyd warshal.
We store the result in a 2D matrix called M.

M[x][y] is the minimum cost to convert letter x into letter y.
The answer will be sum(M[source[i][target[i]] for i in range [0,n-1])
"""

def FloydWarshall(matrix): #Takes in a graph in the form of an adjacency matrix and returns the shortest path for all pairs of nodes. It modifies the matrix.
    n = len(matrix)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        M = [] #M[a][b] is the smallest cost to convert letter a to letter b.

        for _ in range(26):
            M.append([float('inf')] * 26)


        n = len(source)
        mapping = {c:ord(c) - ord('a') for c in string.ascii_lowercase} #map each letter to a number.

        for i in range(26):
            M[i][i] = 0

        for u,v,w in zip(original, changed, cost):
            firstLetter = mapping[u]
            secondLetter = mapping[v]
            M[firstLetter][secondLetter] = min(w, M[firstLetter][secondLetter])

        #Now we use Floyd_Warshall

        FloydWarshall(M) #Now M[a][b] has the smallest cost to convert letter a to letter b.


        answer = 0

        for i in range(n):
   
            firstLetter = mapping[source[i]]
            secondLetter = mapping[target[i]]
            answer += M[firstLetter][secondLetter]

        if answer == float('inf'): #There is no solution
            return -1
        return answer