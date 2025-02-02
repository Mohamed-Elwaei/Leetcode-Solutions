"""
Graph coloring problem.

"""

RED = 1
GREEN = 2
BLUE = 3
BLACK = 4
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u,v in paths:
            u -= 1
            v -= 1
            graph[u].append(v)
            graph[v].append(u)
        

        coloring = [0] * n

        def dfs(u):

            colors_available = {RED, GREEN, BLUE, BLACK}
            for v in graph[u]:
                colors_available -= {coloring[v]}
            
            if len(colors_available) == 0:
                return 
            coloring[u] = next(iter(colors_available))
            for v in graph[u]:
                if coloring[v] == 0:
                    dfs(v)
        
        for u in range(n):
            if coloring[u] == False:
                dfs(u)
  

        return coloring
        