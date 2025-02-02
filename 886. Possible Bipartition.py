class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        V,E = n, len(dislikes)
        graph = {node:[] for node in range(V+1)}
        for u,v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        

        colors = [0] * (V+1)
        visited = set()
        def dfs(u):
            if colors[u] == 0:
                colors[u] = 1
            visited.add(u)
            for v in graph[u]:
                if colors[v] == colors[u]: 
                    return False
                colors[v] = -colors[u]
                if v not in visited and not dfs(v):
                    return False
            return True
        for v in range(V):
            if not dfs(v): return False
        return True