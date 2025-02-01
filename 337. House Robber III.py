# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):              #With root, Without root
            if node == None: return [0,0]
            leftSubtree = dfs(node.left)
            rightSubtree = dfs(node.right)
            withoutRoot = max(leftSubtree) + max(rightSubtree)
            withRoot = leftSubtree[1] + rightSubtree[1] + node.val
            return [withRoot, withoutRoot]
        return max(dfs(root))