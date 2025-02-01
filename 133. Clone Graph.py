"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque,defaultdict
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        queue = deque([node])
        graph = dict()
        start = node
        visited = set()
        visited.add(node)
        if not start:
            return 
        while queue:
            u = queue.popleft()
            graph[u.val] = [n.val for n in u.neighbors]

            for v in u.neighbors:
                if v not in visited:
                    queue.append(v)
                    visited.add(v)
        
        copyNodes = {n:Node(n) for n in graph.keys()}

        for u in graph:
            for v in graph[u]:
                copyNodes[u].neighbors.append(copyNodes[v])
        return copyNodes[start.val]


        

        return [[]]


            