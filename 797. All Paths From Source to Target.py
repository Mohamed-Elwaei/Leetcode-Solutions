class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        V = len(graph)
        paths = []
        path = [0]
        def dfs():
            curr = path[-1]
            if curr == V-1:
                paths.append(path[:])
            else:
                for neighbour in graph[curr]:
                    path.append(neighbour)
                    dfs()
                    path.pop()
        dfs()
        return paths