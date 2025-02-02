# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(set)

        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            graph[root].add(root.left)
            graph[root].add(root.right)
            if root.right:
                graph[root.right].add(root)
            if root.left:
                graph[root.left].add(root)
            inorder(root.right)
        inorder(root)
        tmp = dict()
       
        for node in graph:
            tmp[node.val] = set()
            for x in graph[node]:
                if x:
                    tmp[node.val].add(x.val)
        graph = tmp
        visited = set()
        queue = deque([(start,0)])
        while queue:
            curr,dist = queue.popleft()
            visited.add(curr)
            for neighbour in graph[curr]:
                if neighbour not in visited:
                    queue.append((neighbour,dist+1))
        return dist
