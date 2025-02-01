# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        ordered=[]
        def inorder(root):
            if not root: return 

            inorder(root.left)
            ordered.append(root.val)
            inorder(root.right)
        
        inorder(root)
        return ordered[k-1]

        