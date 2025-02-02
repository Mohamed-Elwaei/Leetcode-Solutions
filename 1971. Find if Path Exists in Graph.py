class Solution(object):
    def DFS(self,source,graph,visited):
        if source in visited:
            return
        else: visited.add(source)
        
        for v in graph[source]:
            self.DFS(v,graph,visited)
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        graph=defaultdict(lambda:set())
        visited=set()
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
        self.DFS(source,graph,visited)
        if destination in visited:
            return True
        else :return False
    
    
            