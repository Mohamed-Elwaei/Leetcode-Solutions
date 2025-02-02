# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import namedtuple
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        levels = {}
        def dfs(node = root, lvl = 0,pos = 1):
            if not node: return
            if lvl not in levels:
                levels[lvl] = [pos,pos]
            else:
                levels[lvl][0] = min(levels[lvl][0],pos)
                levels[lvl][1] = max(levels[lvl][1],pos)
            dfs(node.left, lvl + 1, pos*2)
            dfs(node.right, lvl + 1, pos*2 + 1)
        dfs()
        ans = 0
        for Min,Max in levels.values():
            ans = max(Max - Min + 1, ans)
        return ans