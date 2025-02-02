# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        ans= [None]
        def inorder(o,c):
            if not o:
                return None
            inorder(o.left,c.left)
            if o.val == target.val:
                ans[0]=c
                return

            inorder(o.right,c.right)
        
        inorder(original,cloned)
        return ans[0]
        