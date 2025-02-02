"""
We are looking at a rooted tree (graph).
The tree is rooted at headID.

We do a BFS (or DFS) to determine the amount of time needed to inform all imployees
"""
from collections import deque

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = [[] for _ in range(n)]  #first we build the graph
        root = headID

        for i in range(n):
            if i == root: continue
            u,v = i, manager[i]
            graph[u].append(v)
            graph[v].append(u)

        

        

        visited = [False] * n
        def bfs(root):
            
            queue = deque([[0, root]]) #informTime + node
            answer = 0
            while queue:
                time, u = queue.popleft()
                answer = max(answer, time)
                visited[u] = True

                for v in graph[u]:
                    if not visited[v]:
                        queue.append((informTime[u] + time, v))
            return answer
        answer = bfs(root)
        return answer