import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        V = len(points)
        for i in range(V):
            points[i] = tuple(points[i])

        start = next(iter(points))
        cost = 0
        heap = []
        manhatten = lambda u,v : abs(u[0] - v[0]) + abs(u[1] - v[1])
        for neighbour in points:
            if points != start:
                heapq.heappush(heap, (manhatten(start, neighbour), start, neighbour))
        visited = set([start])
        while len(visited) < V:
            w,u,v = heapq.heappop(heap)
            if v not in visited:
                visited.add(v)
                cost += w
                for neighbour in points:
                    if neighbour not in visited:
                        heapq.heappush(heap, (manhatten(v, neighbour), v, neighbour))
        return cost