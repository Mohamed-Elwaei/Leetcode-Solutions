"""
We need to find all conneced components in the graph and connect them.

A tree is a graph with n nodes and n-1 edges. The nodes are all connected.

If we have less than n-1 edges, we return -1 as there is no way to make all nodes connected.


Otherwise, we connect the components.

If we have x componentsn with a total of more than or equal to n-1 edges, we need x-1 connections.

Proof:

Base Case:
We have 2 connected components a, and b. a has excess edges. We remove one of the edges and connect it to b.

Inductive step
 P(x): is If we have x componentsn with a total of more than or equal to n-1 edges, we need x-1 connections.

Inductive step would be if P(k) then P(k+1).

Assume P(k) is true. Then we need k-1 connections to make the first k components connected.
We end up with 2 connected components now. One of them must have an excess edge.

We remove the excess edge and connect the two components.
QED

So return the number of components - 1.
"""

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        def dfs(node):
            stack = [node]

            while stack:
                u = stack.pop()
                colors[u] = color

                for v in graph[u]:
                    if colors[v] == 0:
                        stack.append(v)
        

        if len(connections) < n - 1:
            return -1
        

        graph = [[] for _ in range(n)]

        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)

        color = 0
        colors = [0] * n


        for node in range(n):
            if colors[node] == 0:
                color += 1
                dfs(node)
        
        
        return color - 1


    