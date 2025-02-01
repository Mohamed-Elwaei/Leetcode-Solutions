# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        big,small = max(p.val,q.val),min(p.val,q.val)

    
        ans = [None]
        def trav(root):
            if not root:
                return False

            
            if small<=root.val<=big:
                ans[0] = root
                return
            trav(root.left)
            trav(root.right)
        trav(root)
        return ans[0]
