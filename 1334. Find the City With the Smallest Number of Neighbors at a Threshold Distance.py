class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        V,E = n, edges
        matrix = [[float('inf')] * V for _ in range(V)]

        for i in range(V): matrix[i][i] = 0
        for u,v,w in edges:
            matrix[u][v] = matrix[v][u] = w
        
        for k in range(V):
            for i in range(V):
                for j in range(V):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
        
        answer = [float('inf')] * 2

        for u in range(V):
            curr_min = 0
            for v in range(V):
                if matrix[u][v] <= distanceThreshold:
                    curr_min+=1
            if curr_min <= answer[1]:
                answer = [u,curr_min]
        return answer[0]