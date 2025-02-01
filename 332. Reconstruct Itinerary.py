import heapq
class Solution(object):
    def DFS(self,graph,node):

        while ( self.out[node]>0):
            neighbour=heapq.heappop(graph[node])
            self.out[node]-=1
            self.DFS(graph,neighbour)
        self.path.append(node)
        
        
    def findeulerian(self, graph,start):
        # Calculating the no. of in & self.out degrees
        for node in graph:
            self.out[node]+=len(graph[node])
            for neighbour in graph[node]:
                self.ins[neighbour]+=1

        self.DFS(graph,start)
        return self.path[::-1]
        
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        self.graph=defaultdict(list)

        for From,To in tickets:
            heapq.heappush(self.graph[From], To)
            self.graph[To]
        start='JFK'
        self.ins={node: 0 for node in self.graph}
        self.out={node: 0 for node in self.graph}

        stack=[start]
        self.path=[]
        return self.findeulerian(self.graph,start)
            


        

        