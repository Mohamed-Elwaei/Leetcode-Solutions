# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nodes = dict()
        def inorder(root):
            if not root: return 
            inorder(root.left)
            nodes[root.val] = nodes.get(root.val, 0 ) + 1
            inorder(root.right)
        inorder(root)

        for n in nodes:
            if k - n in nodes:
                if k - n == n and nodes[n] > 1: return True
                if k - n != n:
                    return True
        return False