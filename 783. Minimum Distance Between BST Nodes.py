# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        last = [None]
        ans = [float('inf')]
        def inorder(root):
            if not root: return
            inorder(root.left)
            if last[0] != None:
                ans[0] = min(ans[0], root.val - last[0])
            last[0] = root.val
            inorder(root.right) 
        inorder(root)
        return ans[0]