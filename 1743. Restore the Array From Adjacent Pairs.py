class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = dict()
        for u,v in adjacentPairs:
            if u in graph:
                graph[u].append(v)
            else:
                graph[u] = [v]
            if v in graph:
                graph[v].append(u)
            else:
                graph[v] = [u]
        
        curr = None
        for u in graph:
            if len(graph[u]) == 1:
                curr = u
        
        array = []
        visited = set()
        while len(array) < len(graph):
            array.append(curr)
            visited.add(curr)

            for v in graph[curr]:
                if v not in visited:
                    curr = v
                    break
        return array