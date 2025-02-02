class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        graph = [[] for _ in range(n)]

        for u,v,w in roads:
            u-=1
            v-=1
            graph[u].append((v,w))
            graph[v].append((u,w))

        visited = [False] * n
        def dfs(node):
            stack = [node]
            answer = float('inf')
            while stack:
                u = stack.pop()
                visited[u] = True
                for v,w in graph[u]:
                    answer = min(w, answer)
                    if not visited[v]:
                        stack.append(v)
            return answer
        
        return dfs(0)