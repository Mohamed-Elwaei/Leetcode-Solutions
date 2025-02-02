class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        V = len(graph)
        colors = [0] * V
        visited = set()
        def dfs(u):
            if colors[u] == 0:
                colors[u] = 1 #Blue
            visited.add(u)
            for v in graph[u]:
                if colors[v] == colors[u]:
                    return False
                colors[v] = -colors[u]
                if v not in visited and not dfs(v): return False
            return True
            
        for v in range(V):
            if not dfs(v):
                return False
        return True