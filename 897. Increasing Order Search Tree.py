# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        curr = [TreeNode()]
        head=curr[0]
        def inorder(root):

            if not root:
                return root
            inorder(root.left)
            curr[0].right=TreeNode()
            curr[0]=curr[0].right
            curr[0].val=root.val
            inorder(root.right)
        
        inorder(root)
        del curr[0]

        return head.right