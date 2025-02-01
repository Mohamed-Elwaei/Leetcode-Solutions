# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        leftLeaves = [0]
        def dfs(root, direction = 'r'):
            if not root: return
            if not root.left and not root.right and direction == 'l':
                leftLeaves[0] += root.val
                return
            dfs(root.left,'l')
            dfs(root.right,'r')
        dfs(root,'r')
        return leftLeaves[0]