class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        graph = {u: [] for u in range(numCourses)}

        for a,b in prerequisites:
            graph[b].append(a)
        
        ins = {u: 0 for u in graph}
        for u in graph:
            for v in graph[u]:
                ins[v]+=1
        
        queue = deque([n for n in graph if ins[n] == 0])
        order = []
        while queue:
            curr=queue.pop()
            order.append(curr)

            for v in graph[curr]:
                ins[v]-=1
                if ins[v] == 0:
                    queue.append(v)
        print(order)
        if len(order) != numCourses:
            return False
        return True
        
        