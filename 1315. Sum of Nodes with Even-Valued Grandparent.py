# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        """
        3 things to keep track of: node, parent, grandparent"""

        answer = 0
        def dfs(node, parent, grandparent):
            nonlocal answer
            if not node:
                return None
            if grandparent and grandparent.val % 2 == 0:
                answer += node.val
            
            dfs(node.left, node, parent)
            dfs(node.right, node, parent)
        dfs(root, None, None)
        return answer