# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        x=root
        y=None
        while x:
            y=x
            if x.val>val:
                x=x.left
            elif x.val<val:
                x=x.right
        if not y:
            root=TreeNode(val=val)
        elif y.val>val:
            y.left=TreeNode(val=val)
        else:
            y.right=TreeNode(val=val)
        return root