"""
We would graph the tree and make it an undirected graph.
We would root the tree at 0 and do a dfs from the root.
We will check each edge we traverse if there is a valid reverse orientation.
If there isn't we reorient the edge and add 1 to the answer.
"""

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        connections = set(tuple([u,v]) for u,v in connections)

        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)

        answer = 0

        def dfs(u, parent):
            nonlocal answer
            for v in graph[u]:
                if v == parent: continue

                if (v,u) not in connections:
                    answer += 1
                dfs(v, u)
        
        dfs(0,-1)
        return answer