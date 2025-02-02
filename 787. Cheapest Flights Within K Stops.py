from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        visited = [float('inf')] * n
        graph = {i:[] for i in range(n)}
        for u,v,w in flights:
            graph[u].append((v,w))

        queue = deque([(src, 0)])
        visited[src] = 0
        k += 1
        while k>0 and queue:
            size = len(queue)
            for _ in range(size):
                node, price = queue.popleft()
                for neigh, ticket in graph[node]:
                    total = price + ticket
                    if total < visited[neigh]:
                        visited[neigh] = total
                        queue.append((neigh, total))
            k-=1
        return visited[dst] if visited[dst]!=float('inf') else -1

            