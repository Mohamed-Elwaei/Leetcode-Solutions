# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ans=[True]
        def dfs(root):
            if not root:
                return 0
            lh = dfs(root.left)
            rh = dfs(root.right)

            if abs(rh-lh) > 1:
                ans[0]=False
                
            return 1+max(rh,lh)
        dfs(root)
        return ans[0]
            