from collections import deque
def sumOfDistancesInTree( n: int, edges: list[list[int]]) -> list[int]:
        graph = dict()
        for a,b in edges:
            if a not in graph:
                graph[a] = [b] 
            else:
                graph[a].append(b)
            if b not in graph:
                graph[b] = [a] 
            else:
                graph[b].append(a)
        
        ret = [None] * len(graph)
        
        def dfs(node):
            visited = set()
            stack = deque([(v,1) for v in graph[node] if v not in visited])
            for n,_ in stack:
                visited.add(n)
            visited.add(node)
            ans = 0
            while stack:
                u,w = stack.popleft()
                ans+=w

                
                for v in graph[u]:
                    if v not in visited:
                        stack.append((v,w+1))
                        visited.add(v)
            return ans
        
        for i in range(n):
            ret[i] = dfs(i)
        return ret

n = 6
edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
print(sumOfDistancesInTree(n,edges))