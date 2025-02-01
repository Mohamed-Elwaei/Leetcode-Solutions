# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        total = [0]
        def postorder(root):
            if not root:
                return 0
            leftVal,rightVal = postorder(root.left), postorder(root.right)
            total[0] += abs(leftVal - rightVal)
            return leftVal + rightVal + root.val
        postorder(root)
        return total[0]
            