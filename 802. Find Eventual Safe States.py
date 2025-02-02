class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:


        memo = dict()

        def dfs(u):
            if u in memo:
                 return memo[u]

            if not graph[u]:
                memo[u] = 'T'
                return memo[u]
            if u in visited:
                 memo[u] = 'C'
                 return memo[u]
            visited.add(u)
            safe = True
            for v in graph[u]:
                 if dfs(v) not in 'ST':
                      safe = False
                 if dfs(v) =='C':
                      memo[u] = 'C'
            if u not in memo:
                 memo[u] = 'S' if safe else 'U'
            return memo[u]
        
        for node in range(len(graph)):
             visited = set()
             dfs(node)
        ret = []
        for node in memo:
             if memo[node] in 'TS':
                  ret.append(node)
        return sorted(ret)