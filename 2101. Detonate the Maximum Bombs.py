"""
You can think of this as a directed graph.

Each node is a bomb and each edge u -> v means bomb u detonates bomb v.

What we can do is a breadth first search from each bomb to find out how many bombs are reachable
"""
from math import sqrt
def distance(x1,y1,x2,y2):

    return sqrt(((x1-x2) ** 2) + ((y1 -y2) ** 2))
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = {i:[] for i in range(n)}


        for i in range(n):
            x1,y1,r1 = bombs[i]
            for j in range(i+1, n):
                x2,y2,r2 = bombs[j]
                d = distance(x1,y1,x2,y2)

                if d <= r1:
                    graph[i].append(j)
                if d <= r2:
                    graph[j].append(i)
        

        def dfs(u):
            stack = [u]
            answer = 1
            
            while stack:
                u = stack.pop()
                visited.add(u)

                for v in graph[u]:
                    if v not in visited:
                        stack.append(v)
                        visited.add(v)
                        answer += 1
            return answer
        
        answer = 0

        for i in range(n):
            visited = set()
            answer = max(dfs(i), answer)
        return answer