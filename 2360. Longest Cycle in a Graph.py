class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        """
        Kosaraju's algorithm.
        Do a dfs to keep track of nodes exit time. 
        Make a transpose copy of the graph.
        Do a dfs from each unvisited node in the graph and get each scc.
        Get the longest scc
        do 2 dfs's
        """
        def dfs(u, stack,graph):
            visited[u] = True
            for v in graph[u]:
                if not visited[v]:
                    dfs(v,stack,graph)
            stack.append(u)


        n = len(edges)
        adj = {i:[] for i in range(n)}
        adjT = {i:[] for i in range(n)}
        for u,v in enumerate(edges):
            if v != -1:
                adj[u].append(v)
                adjT[v].append(u)


        stack = []
        visited = [0] * n
        for u in range(n):
            if not visited[u]:
                dfs(u,stack, adj)
        

        visited = [0] * n
        ans = 0
        while stack:
            u = stack.pop()
            if not visited[u]:
                scc = []
                dfs(u,scc,adjT)
                ans = max(len(scc),ans)
        
        if ans == 1:
            return -1
        else:
            return ans