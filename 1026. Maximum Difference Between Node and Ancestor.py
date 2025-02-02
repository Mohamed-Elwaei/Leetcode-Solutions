# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.diff = 0

        def dfs(root,ancestors=set()):
            if root == None:
                return 
            
            for a in ancestors:
                self.diff = max(self.diff, abs(root.val -  a))
            
            dfs(root.left,ancestors.union({root.val}))
            dfs(root.right,ancestors.union({root.val}))
        dfs(root)
        return self.diff