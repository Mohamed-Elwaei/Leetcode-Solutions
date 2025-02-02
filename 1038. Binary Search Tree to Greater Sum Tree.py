# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        sum = [0]
        def inorder(root):
            if not root: 
                return
            inorder(root.right)
            root.val += sum[0]
            sum[0] = root.val
            inorder(root.left)
        inorder(root)
        return root