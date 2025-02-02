# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(root1,root2):

            if not root1 and not root2:
                return True
            elif not root1 or not root2:
                return False
            elif root1.val != root2.val:
                return False

            left1 = None if not root1.left else root1.left.val
            left2 = None if not root2.left else root2.left.val
            right1 = None if not root1.right else root1.right.val
            right2 = None if not root2.right else root2.right.val

            if left1 == right2 and left2 == right1:
                root1.left,root1.right = root1.right, root1.left
            return dfs(root1.left,root2.left) and dfs(root1.right, root2.right)

        return dfs(root1,root2)
