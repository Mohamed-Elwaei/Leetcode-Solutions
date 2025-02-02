"""

We have the same amount of nodes and edges.
Find all strongly connected components, and form a condensation graph.

In a condensation graph, each node is a strongly connected component, and there are no cycles.
A node can atleast visit all of the nodes in the scc it is contained in.

Consider the bridge edges. Bridge edges connect scc together.
If a node u has an edge u -> v that is a bridge edge, then u and v are in different sccs.

So then ans[u] = max(scc(u), 1 + ans[v]).

In the condensation graph. let u and v be different condensation graphs.
if v is reachable from u, then ans[u] = size(u) + ans[v].
for each node in u ans[node] = ans[u]. 
Except if the node has a bridge, 
in that case ans[node] = max(size(scc(node)), 1 + size(scc(node that bridge points to)))


Condensation graph is then a directly acyclic graph, meaning it can be topologically sorted.
let bottom be the bottom most node in the topoligical sort. Then ans[bottom] = size(scc(bottom)). 
Because no other node in the condensation graph is reachable.

"""
from collections import deque

class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
       
        n = len(edges)
        GF, GR = [[] for _ in range(n)], [[] for _ in range(n)]

        for u,v in enumerate(edges):
            GF[u].append(v)
            GR[v].append(u)
        
        order = []
        comp = []
        vis = [0] * n
        color = 0
        nodeMap = [0] * n

        def dfs1(u):
            vis[u] = 1
            for v in GF[u]:
                if not vis[v]:
                    dfs1(v)
            order.append(u)
        
        def dfs2(u):
            vis[u] = 1
            comp.append(u)
            for v in GR[u]:
                if not vis[v]:
                    dfs2(v)
            return

        for u in range(n):
            if not vis[u]:
                dfs1(u)
        
        order = order[::-1]
        vis = [0] * n
        sccSize = []

        for u in order:
            if not vis[u]:
                dfs2(u)
                sccSize.append(len(comp))

                for v in comp:
                    nodeMap[v] = color
                color+=1
                comp = []


        adj_cond = [set() for _ in range(color)] 
        indegrees = [0] * color
        for u in range(n):
            for v in GF[u]:
                if nodeMap[v] != nodeMap[u]:
                    adj_cond[nodeMap[u]].add(nodeMap[v])
                    
        for u in range(color):
            for v in adj_cond[u]:
                indegrees[v]+=1

        order = [] #Topological ordering of the condensation graph
        queue = deque([i for i in range(color) if indegrees[i] == 0])

        while queue:
            u = queue.popleft()
            order.append(u)

            for v in adj_cond[u]:
                indegrees[v]-=1
                if indegrees[v] == 0:
                    queue.append(v)

        
        for u in order[::-1]:
            tmp = sccSize[u]
            for v in adj_cond[u]:
                tmp = max(tmp, sccSize[u] + sccSize[v])
            sccSize[u] = tmp

        

        ans = [0] * n
        vis = [0] * n
        def dfs3(u):
            vis[u] = 1
            ans[u] = sccSize[nodeMap[u]]

            for v in GF[u]:
                if nodeMap[u] != nodeMap[v]:
                    if not vis[v]:
                        dfs3(v)
                    ans[u] = max(ans[u], 1 + ans[v])
        for u in range(n):
            if not vis[u]: dfs3(u)
            
        return ans