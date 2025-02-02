class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        V = n

        DP = [[float('inf')] * V for _ in range(V)]

        DP[x-1][y-1] = DP[y-1][x-1] = 1
        for u in range(V):
            if u+1 < V:
                DP[u][u+1] = DP[u+1][u] = 1
            DP[u][u] = 0    

        # for row in DP:
        #     print(row)

        for k in range(V):
            for i in range(V):
                for j in range(V):
                    DP[i][j] = min(DP[i][j], DP[i][k] + DP[k][j])
        
        for row in DP:
            print(row)
        result = [0] * V
        for u in range(V):
            for v in range(V):
                k = DP[u][v]
                if k > 0:
                    result[k-1] += 1
        return result