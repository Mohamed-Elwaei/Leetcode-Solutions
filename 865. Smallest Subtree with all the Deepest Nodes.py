# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        #   3
        # 1   2
        #1       4

        #    3
        #  1   2
        #1       4
        #       2  1
        ret = None
        maxLevel = 0
        def depth(root, level):
            nonlocal ret, maxLevel
            if not root: return level
            leftDepth = depth(root.left, level + 1)
            rightDepth = depth(root.right, level + 1)
            if leftDepth == rightDepth and maxLevel <= leftDepth:
                maxLevel = leftDepth
                ret = root
            return max(leftDepth, rightDepth)
        depth(root, 0)
        return ret