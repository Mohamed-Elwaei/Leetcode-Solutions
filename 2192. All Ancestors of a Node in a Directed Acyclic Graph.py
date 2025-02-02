from collections import deque
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ins = {i:0 for i in range(n)}
        graph = {i:[] for i in range(n)}
        ancestors = {i:set() for i in range(n)}
        for u,v in edges:
            graph[u].append(v)
            ins[v] += 1
        
        queue = deque([node for node in range(n) if ins[node] == 0])
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                ins[v] -= 1
                if ins[v] == 0:
                    queue.append(v)
                ancestors[v].add(u)
                ancestors[v] = ancestors[v].union(ancestors[u])
        ancestors = [sorted(list(ancestors[node])) for node in range(n)]
        return ancestors