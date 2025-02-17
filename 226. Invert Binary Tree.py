# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        inorder=[]
        def traverse(root):
            if not root:
                return
            root.right,root.left = traverse(root.left),traverse(root.right)

            return root
        traverse(root)
        return root