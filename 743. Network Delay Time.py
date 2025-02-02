import heapq
class Solution(object):
    def shortestPath(self,graph,start):
        ordered=self.topsort(graph)
        distances={node: float('inf') for node in graph}
        distances[start]
        for node in ordered:
            for neighbour in graph[node]:
                weight=graph[node][neighbour]
                new_distance=distances[node]+weight
                if new_distance<distances[neighbour]:
                    distances[neighbour]=new_distance
        return distances   
    def DFS(self,node,graph,visited,stack):
        visited.add(node)

        for neighbour in graph[node].keys():
            if neighbour not in visited:
                self.DFS(neighbour,graph,visited,stack)
        stack.append(node)
    def topsort(self,graph):
        visited=set()
        stack=[]

        for node in graph:
            if node not in visited:
                self.DFS(node,graph,visited,stack)
        return stack[::-1]
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        distances=[float('inf')] * (1+n)
        distances[k] = 0
        for _ in range(n):
            for u,v,w in times:
                distances[v] = min(distances[v], distances[u] + w)
        
        ans=max(distances[1:])

        if ans!=float('inf'):
            return ans
        else: return -1

