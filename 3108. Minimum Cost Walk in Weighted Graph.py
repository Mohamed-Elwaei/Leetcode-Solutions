from collections import deque
class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        """
        AND & is monotinacally decreasing.
        If two nodes are not in the same component, return -1.
        Since and in monotinacally decreasing, 
        Else return the edges in the component anded together.
        
          4.  0
        1 - 2 - 3
        """
        graph = {i:[] for i in range(n)} #Node => Edges
        for u,v,w in edges:
            graph[u] += [(v,w)]
            graph[v] += [(u,w)]
        
        def bfs(u, color):
            
            cost = -1
            queue = deque([[u,-1]])
            while queue:
                u, w = queue.popleft()
                cost &= w
                colors[u] = color
                for v,w in graph[u]:
                    if colors[v] != -1: continue
                    queue.append((v,w))
            costs[color] = cost
                    
            
        colors = [-1] * n
        component = 0
        costs = {} #Map each component to edges anded together
        for node in graph:
            if colors[node] == -1:
                bfs(node, component)
                component += 1
        
        
        answer = []
        for u,v in query:
            if colors[u] != colors[v]: #Not reachable
                answer.append(-1)
            else:
                answer.append(costs[colors[u]])
        return answer
                