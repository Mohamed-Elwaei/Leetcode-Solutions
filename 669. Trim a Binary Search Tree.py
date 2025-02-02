# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def modify(root):

            if root:
                root.left = modify(root.left)
                root.right = modify(root.right)
            while root and root.val < low:
                root = root.right
            while root and root.val > high:
                root = root.left
            return root
        root = modify(root)
        return root