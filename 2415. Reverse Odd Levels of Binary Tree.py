# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reverse():
            N = len(queue)
            l,r = 0, N - 1
            while l < r:
                queue[l].val, queue[r].val = queue[r].val, queue[l].val
                l += 1
                r -= 1
            


        queue = deque([root])
        odd = 0

        while queue:
            if odd:
                reverse()
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            queue.extend(level)
            odd ^= 1
        return root