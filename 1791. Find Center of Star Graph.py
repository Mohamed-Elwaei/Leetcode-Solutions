from collections import defaultdict
class Solution(object):

    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        a=set(edges[0])
        b=set(edges[1])
        return min(a.intersection(b))
        # nodes=set()
        # graph=defaultdict(lambda :set())
        # ans=0
        # for e in edges:
        #     nodes.add(e[0])
        #     nodes.add(e[1])
        #     graph[e[0]].add(e[1])
        #     graph[e[1]].add(e[0])
        # for v in graph:
        #     if len(graph[v])==len(nodes)-1:
        #         return v