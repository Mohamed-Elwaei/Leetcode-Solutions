from collections import defaultdict
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        V = numCourses
        graph = [[float('inf')]  * V for _ in range(V)]
        for i in range(V):
            graph[i][i] = 1
        for u,v in prerequisites:
            graph[u][v] = 1
        
        for k in range(V):
            for i in range(V):
                for j in range(V):
                    graph[i][j] = min(graph[i][j],graph[i][k] + graph[k][j])
        
        return [graph[a][b]!=float('inf') for a,b in queries]
       