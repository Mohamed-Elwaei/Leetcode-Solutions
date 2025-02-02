class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        def dfs(u):
            colors[color] += 1
            visited.add(u)
            for v in graph[u]:
                if v not in visited:
                    dfs(v)

        graph = {i:[] for i in range(n)}
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        colors = {}
        color = 0
        visited = set()
        for node in range(n):
            if node not in visited:
                color += 1
                colors[color] = 0
                dfs(node)
        pairs = 0
        for color, size in colors.items():
            n -= size
            pairs += size * n
        return pairs