from typing import List

class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.mat = [[float('inf')] * n for _ in range(n)]
        
        for i in range(n):
            self.mat[i][i] = 0
        
        for u, v, w in edges:
            self.mat[u][v] = w
        
        self._floyd_warshall()

    def _floyd_warshall(self):
        n = self.n
        mat = self.mat
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if mat[i][k] < float('inf') and mat[k][j] < float('inf'):
                        mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])

    def addEdge(self, edge: List[int]) -> None:
        u, v, w = edge
        if self.mat[u][v] > w:
            self.mat[u][v] = w
            for i in range(self.n):
                for j in range(self.n):
                    if self.mat[i][u] < float('inf') and self.mat[v][j] < float('inf'):
                        self.mat[i][j] = min(self.mat[i][j], self.mat[i][u] + w + self.mat[v][j])

    def shortestPath(self, node1: int, node2: int) -> int:
        if self.mat[node1][node2] == float('inf'):
            return -1
        else:
            return self.mat[node1][node2]

# Example usage:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1, node2)