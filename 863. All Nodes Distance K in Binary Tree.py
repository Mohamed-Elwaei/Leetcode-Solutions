# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = {}
        def dfs(root):
            if root.left:
                graph[root] = graph.get(root,[]) + [root.left]
                graph[root.left] = graph.get(root.left, []) + [root]
                dfs(root.left)
            if root.right:
                graph[root] = graph.get(root,[]) + [root.right]
                graph[root.right] = graph.get(root.right, []) + [root]
                dfs(root.right)
        dfs(root)
        if target not in graph:
            return []
        queue = deque([[target,0]])
        nearby = []
        visited = set()
        while queue:
            node,lvl = queue.popleft()
            visited.add(node)
            if lvl == k:
                nearby.append(node.val)
                continue
            for neigh in graph[node]:
                if neigh not in visited:
                    queue.append([neigh,lvl + 1])
        return nearby