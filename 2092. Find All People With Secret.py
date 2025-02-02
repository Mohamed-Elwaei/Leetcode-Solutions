from collections import defaultdict

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key = lambda x: x[2])
        graphs = dict() #time => graph

        for u,v,t in meetings:
            graphs[t] = graphs.get(t,defaultdict(list))
            graphs[t][u].append(v)
            graphs[t][v].append(u)
        
        holders = set([0,firstPerson])
        def dfs(u,time):
            if u in visited:
                return
            visited.add(u)
            holders.add(u)
            for v in graphs[time][u]:
                dfs(v,time)
        for time in graphs:
            visited = set()
            for node in graphs[time]:
                if node in holders:
                    dfs(node,time)
        return holders