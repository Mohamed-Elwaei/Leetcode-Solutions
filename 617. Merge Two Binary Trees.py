# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if not root1 and not root2: return
        root3=TreeNode()
        if not root1:
            root1=TreeNode()
        if not root2:
            root2=TreeNode()
        def inorder(root1,root2,root3):
            a=0
            b=0

            if root1:
                a+=root1.val
            if root2:
                b+=root2.val
            
  
            if root1.left or root2.left:
                root3.left =TreeNode()
                if root2.left and root1.left:
                    inorder( root1.left,root2.left,root3.left)
                elif root2.left:
                    inorder(TreeNode(),root2.left,root3.left)
                elif root1.left:
                    inorder(root1.left,TreeNode(),root3.left)
            root3.val = a+b

            if root1.right or root2.right:
                root3.right =TreeNode()
                if root2.right and root1.right:
                    inorder( root1.right,root2.right,root3.right)
                elif root2.right:
                    inorder(TreeNode(),root2.right,root3.right)
                elif root1.right:
                    inorder(root1.right,TreeNode(),root3.right)
            
        inorder(root1,root2,root3)
        return root3