# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def evaluateTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def inorder(root):
            if not root.right and not root.left:
                return root.val
            
            if root.val == 2:
                return inorder(root.left) | inorder(root.right)
            else:
                return inorder(root.left) & inorder(root.right)
        return inorder(root)
        