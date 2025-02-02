import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], s: int, e: int) -> float:
        graph = {i:[] for i in range(n)}
        for (u,v),w in zip(edges, succProb):
            graph[u] = graph.get(u,[]) + [(v,w)]
            graph[v] = graph.get(v,[]) + [(u,w)]

        processed = [0] * n
        probs = [0] * n
        probs[s] = 1
        queue = [(-1,s)]
        print(graph)
        while queue:
            u = heapq.heappop(queue)[1]
            if processed[u]: continue
            processed[u] = 1
            for v,w in graph[u]:
                if probs[u] * w > probs[v]:
                    probs[v] = probs[u] * w
                    heapq.heappush(queue, (-probs[v],v))
        return probs[e]