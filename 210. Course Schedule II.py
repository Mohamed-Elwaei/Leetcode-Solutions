class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        graph = {n:[] for n in range(numCourses)}
        ins = {n:0 for n in range(numCourses)}
        for a,b in prerequisites:
            graph[b].append(a)
            
        for u in graph:
            for v in graph[u]:
                ins[v]+=1
        
        queue = deque([n for n in range(numCourses) if ins[n] == 0])
        order = []
        while queue:
            curr = queue.pop()
            order.append(curr)

            for v in graph[curr]:
                ins[v]-=1
                if not ins[v]:
                    queue.append(v)

        if len(order) != len(graph):
            return []
        return order