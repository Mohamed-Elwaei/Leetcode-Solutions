from collections import defaultdict, deque

def check_cycle(graph, V): #Return a boolean indicating if there is a cycle in a graph
    colors = [0] * V
    flag = 0

    def dfs(u):
        nonlocal flag
        if flag == 1:  # Early return if cycle is found
            return
        colors[u] = 1

        for v in graph[u]:
            if colors[v] == 1:
                flag = 1
                return
            elif colors[v] == 0:
                dfs(v)

        colors[u] = 2
    
    for u in range(V):
        if colors[u] == 0:
            dfs(u)
    
    return flag == 1

def topological_sort(graph, V):
    in_degrees = [0] * V
    for u in range(V):
        for v in graph[u]:
            in_degrees[v] += 1
    
    queue = deque([u for u in range(V) if in_degrees[u] == 0])
    ret = []
    
    while queue:
        u = queue.popleft()
        ret.append(u)
        for v in graph[u]:
            in_degrees[v] -= 1
            if in_degrees[v] == 0:
                queue.append(v)

    return ret 

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        V = k

        graph_vertical = [[] for _ in range(V)]
        graph_horizontal = [[] for _ in range(V)]

        for u, v in rowConditions:
            u -= 1
            v -= 1
            graph_vertical[u].append(v)
        for u, v in colConditions:
            u -= 1
            v -= 1
            graph_horizontal[u].append(v)
        
        if check_cycle(graph_vertical, V) or check_cycle(graph_horizontal, V):
            return []

        rowIndices = topological_sort(graph_vertical, V)
        colIndices = topological_sort(graph_horizontal, V)

        if not rowIndices or not colIndices:  # Check if a valid topological sort exists
            return []

        # Mapping number to its topological sort index
        row_pos = {num: i for i, num in enumerate(rowIndices)}
        col_pos = {num: i for i, num in enumerate(colIndices)}

        matrix = [[0] * V for _ in range(V)]
        
        for num in range(V):
            matrix[row_pos[num]][col_pos[num]] = num + 1
        
        return matrix