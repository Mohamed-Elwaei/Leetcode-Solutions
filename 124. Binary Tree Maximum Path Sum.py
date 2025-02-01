# Definition for a binary tree root.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
For each node, calculte the maximum path going downward.

Each path has a 'highest point'.

Calculate the maximum value for each node being a highest point.


max(node) = (node.val, node.val + maxDepthLeft, node.val + maxDepthRight, node.val + maxDepthRight)
"""

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        

        answer = float('-inf')

        def dfs(root):
            nonlocal answer
            if root == None:
                return 0
            left = dfs(root.left) 
            right = dfs(root.right)

            answer = max(answer, left + right + root.val)

            return max(left + root.val, right + root.val, 0)
        dfs(root)
        return answer