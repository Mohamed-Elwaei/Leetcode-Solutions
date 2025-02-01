# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        memo = dict() #node to p
        self.paths = 0

        def dfs(root):
            if root == None:
                return []
            ways = [root.val]            
            ways.extend([root.val + x for x in dfs(root.left) + dfs(root.right)])
            for w in ways:
                self.paths+= w==targetSum
            return ways
        dfs(root)
        return self.paths