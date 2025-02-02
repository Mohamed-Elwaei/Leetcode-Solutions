"""
Base case if there is only 1 node. Return 0.

Otherwise we want to know what the size of each tree is.

we wil do a dfs starting from the root (node 0).
on the end of the dfs from node u we will calculate the size of the tree rooted at u.
we then divide that size by seats and ceil the result. and add it to the answer. 
we then subtract the size of the entire tree from the answer, in order not to overcount.

"""

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        V = len(roads) + 1
        graph = [[] for _ in range(V)]
        

        for u,v in roads:
            graph[u].append(v)
            graph[v].append(u)

        answer = 0
        def dfs(u, parent): 
            nonlocal seats, answer 
            size = 1

            for v in graph[u]:
                if v == parent: 
                    continue   
                size += dfs(v, u)
                
            
            if u != 0:
                answer += ceil(size / seats)
            return size
        dfs(0,-1)

        return answer