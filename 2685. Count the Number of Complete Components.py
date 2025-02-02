
class Solution(object):
    def countCompleteComponents(self, n, edges):
            """
            :type n: int
            :type edges: List[List[int]]
            :rtype: int
            """
            def dfs(u):
                visited.add(u)
                flag = True
                for v in graph[u]:
                    if v not in visited:
                        if graph[v] != graph[u]:
                            flag = False
                        flag = dfs(v) & flag
                return flag

            graph = {i:set([i]) for i in range(n)}
            for u,v in edges:
                graph[u].add(v)
                graph[v].add(u)
            
            visited = set()
            components = 0
            for node in range(n):
                if node not in visited:
                    components += dfs(node)
            return components

        