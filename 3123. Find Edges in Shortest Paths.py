import heapq

"""
We wanna use a version of djikstra.
We want to keep track of all possible predecessors.
We store that in 2D array called predecessor.

if predecessor[v] = [u1,u2,...,uk]
then the shortest path for v is equal to:
shortest path to u1 + weight of edge (u1,v)
shortest path to u2 + weight of edge (u2,v)
        ..........
shortest path to uk + weight of edge (uk,v)

So that means we include edges (u1,v), (u2,v) ... (uk,v).
After that we add all edges in the shortest path from node 0 to nodes u1, u2, ... uk until we reach node 0.

"""


import heapq
def Djikstra(graph, start):#djikstra will return the 2D array predecessors
    V = len(graph)

    processed = [False] * V
    distances = [float('inf')] * V
    distances[start] = 0
    predecessors = [[] for _ in range(V)]

    heap = [(0,start)]

    while heap:
        _, u = heapq.heappop(heap)
        if processed[u]: continue
        processed[u] = True

        for v,w in graph[u]:
            if w + distances[u] < distances[v]:
                predecessors[v] = [u]
                distances[v] = w + distances[u]
                heapq.heappush(heap, (distances[v], v))
            elif w + distances[u] == distances[v]:
                predecessors[v].append(u)
    return distances, predecessors


class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        V,E = n, len(edges)
        graph = [[] for _ in range(V)]

        for u,v,w in edges:
            graph[u].append((v,w))
            graph[v].append((u,w))
        
        S = set()
        visited = [False] * V

        distances, predecessors = Djikstra(graph, 0)

        def dfs(u):
            if visited[u]:
                return 
            visited[u] = True
            for parent in predecessors[u]:
                S.add((u,parent,distances[u] - distances[parent]))
                S.add((parent,u,distances[u] - distances[parent]))
                dfs(parent)
        
        dfs(V-1)


        answer = [False] * E

        for i in range(E):
            u,v,w = edges[i]
            if (u,v,w) in S:
                answer[i] = True
            
            elif (v,u,w) in S:
                answer[i] = True
        return answer