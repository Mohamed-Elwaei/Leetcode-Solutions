# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        answer = root.val
        while queue:
            answer = sum([node.val for node in queue])
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            queue.extend(level)
        return answer