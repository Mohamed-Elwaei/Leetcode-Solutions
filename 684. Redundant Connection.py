from collections import deque
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:



        mapping = {}
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for i,(a,b) in enumerate(edges):
            mapping[a,b] = i
            graph[a].append(b)
            graph[b].append(a)
        
        ans = (-1,-1)
        def bfs(graph, root):
            nonlocal n, ans
            visited = [False] * n
            queue = deque([[root,-1]])
            while queue:
                u,par = queue.popleft()
                visited[u] = True
            
                for v in graph[u]:
                    edge = (u,v)

                    if edge not in mapping:
                        edge = (v,u)

                    if par == v: continue

                    if visited[v]:

                        if ans == (-1,-1) or mapping[ans] < mapping[edge]:
                            ans = edge
                    else:
                        queue.append([v,u])
            
        for u in range(1,n):
            bfs(graph, u)
        return ans