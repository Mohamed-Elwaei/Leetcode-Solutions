# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def postorder(root):
            if root == None: return 0

            left = postorder(root.left)
            right = postorder(root.right)
            if left == 0:
                root.left = None
            if right == 0:
                root.right = None
            return left | root.val | right
            
        if postorder(root) == 0: return None
        return root
