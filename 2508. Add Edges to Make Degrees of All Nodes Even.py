from typing import List

class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        G = [set() for _ in range(n + 1)]
        degrees = [0] * (n + 1)
        
        for u, v in edges:
            G[u].add(v)
            G[v].add(u)
            degrees[u] += 1
            degrees[v] += 1
        
        odds = [i for i in range(1, n + 1) if degrees[i] % 2 == 1]
        
        if len(odds) == 0:
            return True
        
        if len(odds) == 2:
            u, v = odds
            if u not in G[v]:
                return True
            for i in range(1, n + 1):
                if i != u and i != v and i not in G[u] and i not in G[v]:
                    return True
            return False
        
        if len(odds) == 4:
            u, v, x, y = odds
            if (u not in G[v] and x not in G[y]) or (u not in G[x] and v not in G[y]) or (u not in G[y] and v not in G[x]):
                return True
            return False
        
        return False