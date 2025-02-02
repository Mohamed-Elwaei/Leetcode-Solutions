"""
This looks like a single-source shortest path problem.
We can use djikstra's algorithm.

We modify djikstra to detect if each node can be visited before it disappears.
"""

    
import heapq
class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        
        if disappear[0] <= 0: return [-1] * n
        
        graph = [[] for _ in range(n)]
        
        for u,v,w in edges:
            graph[u].append((v,w))
            graph[v].append((u,w))
        
        
        
        distance = [float('inf')] * n
        visited = [False] * n
        
        heap = [(0,0)] #Priority queue. It stores a pair of the distance and node.
        distance[0] = 0
        
        
        while heap:
            u = heap[0][1]
            heapq.heappop(heap)
            
            if visited[u]: continue
            visited[u] = 1
            
            
            for v,w in graph[u]:
                
                if distance[v] > distance[u] + w and distance[u] + w < disappear[v]:
                    distance[v] = distance[u] + w
                    heapq.heappush(heap, (distance[v],v))
        
        
        answer = []
        for x in distance:
            if x == float('inf'):
                answer.append(-1)
            else:
                answer.append(x)
        return answer