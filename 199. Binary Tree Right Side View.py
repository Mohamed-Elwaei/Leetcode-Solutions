# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return

        
        rightSide = [] 

        queue = deque([root])

        while queue:
            rightSide.append(queue[-1].val)
            
            lvl = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    lvl.append(curr.left)
                if curr.right:
                    lvl.append(curr.right)
            queue.extend(lvl[:])
        return rightSide
