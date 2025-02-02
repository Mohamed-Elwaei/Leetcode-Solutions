"""
We root the tree arbitrarily (around 0).
For each subtree rooted at node i, we consider the maximum amount of nodes we can visit.
We do that by using a dfs.
"""

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        V,E = n, len(edges)

        graph = [[] for _ in range(V)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        restricted = set(restricted)


        def dfs(u, parent):
            if u in restricted:
                return 0
            
            answer = 1
            for v in graph[u]:
                if v == parent: continue

                answer += dfs(v, u)
            return answer
                
        
        return dfs(0,-1)