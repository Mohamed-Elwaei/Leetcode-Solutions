"""
We can remove at most n-1 stones.


For every connected component we can remove x-1 stones, where x is the size of the component.


let P(k) be the predicate that we can remove k-1 stones from a component of size k

Base case: P(1) we remove 0 stones.

Inductive step: If P(k) then P(k+1)

Assume P(k) is true. that means we can remove k-1 nodes from the component.

If we have a component of size k+1, then we can remove k-1 nodes, and be left with 2 nodes.

We can do it in a way that at the end the 2 nodes are connected.
"""


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        graph = {}
        
        def dfs(node,color):
            stack = [node]
            
            
            
            while stack:
                node = stack.pop()
                colors[node] = color
                for neigh in graph[node]:
                    if neigh not in colors:
                        stack.append(neigh)
            
        
        for i,(x,y) in enumerate(stones):
            
            for j,(u,v) in enumerate(stones[i+1:]):
                if u == x or v == y:
                    graph[x,y] = graph.get((x,y),[]) + [(u,v)]
                    graph[u,v] = graph.get((u,v),[]) + [(x,y)]
            
        colors = {}
        num_components = 0
        for node in graph:
            if node not in colors:
                dfs(node, num_components)
                num_components += 1
        
        
        component_size = [0] * num_components
        
        for node in colors:
            component_size[colors[node]] += 1
        
        return sum(component_size) - num_components
                