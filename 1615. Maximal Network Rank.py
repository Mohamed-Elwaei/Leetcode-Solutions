class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = {i:set() for i in range(n)}
        for a,b in roads:
            graph[a].add((a,b))
            graph[b].add((a,b))
        biggest = set()
        for u in graph:
            for v in graph:
                tmp = graph[u].union(graph[v])
                if len(tmp) > len(biggest):
                    biggest = tmp
        return len(biggest)