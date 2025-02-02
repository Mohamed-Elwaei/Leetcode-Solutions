from collections import deque
from typing import List

def shortestPath(graph, start):
    n = len(graph)
    distances = [-1] * n
    distances[start] = 0

    queue = deque([start])
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if distances[v] != -1: 
                continue
            queue.append(v)
            distances[v] = distances[u] + 1
    return distances

class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        n = len(patience)

        # Create graph
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Calculate shortest path from the master server (node 0) to all other servers
        distances = shortestPath(graph, 0)

        # Calculate the time when the network becomes idle
        max_time = 0
        for i in range(1, n):
            time_to_master = distances[i] * 2
            if patience[i] < time_to_master:
                last_resend_time = ((time_to_master - 1) // patience[i]) * patience[i]
                last_message_arrival_time = last_resend_time + time_to_master
            else:
                last_message_arrival_time = time_to_master

            max_time = max(max_time, last_message_arrival_time)

        return max_time + 1