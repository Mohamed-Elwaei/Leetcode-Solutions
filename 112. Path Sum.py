# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return 
        targetSum-=root.val
        if targetSum==0 :
            if not root.left and not root.right:
                return True

        x= self.hasPathSum(root.left,targetSum)    
        y= self.hasPathSum(root.right,targetSum) 
        if x==True or y==True:
            return True
        