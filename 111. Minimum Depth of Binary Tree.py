# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        x=self.minDepth(root.left)+1
        y=self.minDepth(root.right)+1

        if x<=1:
            return y
        elif y<=1:
            return x
        else:
            return min(x,y)        