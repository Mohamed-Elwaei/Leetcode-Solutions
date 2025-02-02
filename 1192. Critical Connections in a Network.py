




class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        G = [[] for _ in range(n)]

        for (u,v) in connections:
            G[u].append(v)
            G[v].append(u)
        
        lows =  [-1] * n
        ids = [-1] * n
        id = 1
        vis = [0] * n
        bridges = []
        def dfs(u, par):
            nonlocal id, bridges, vis, ids, lows
            vis[u] = 1
            ids[u] = lows[u] = id
            id+=1

            for v in G[u]:
                if v == par: continue
                elif vis[v]:
                    lows[u] = min(lows[u], lows[v])
                else:
                    dfs(v,u)
                    lows[u] = min(lows[u], lows[v])
                    if ids[u] < lows[v]:
                        bridges.append((u,v))
        
        for i in range(n):
            if not vis[i]:
                dfs(i,-1)
        return bridges