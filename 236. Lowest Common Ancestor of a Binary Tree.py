# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        LCA = None
        def postorder(root):
            nonlocal LCA
            if root == None:
                return None
            left = postorder(root.left)
            right = postorder(root.right)
            if root == p:
                if right not in {p,q}: right = p
                elif left not in {p,q}: left = p
            if root == q:
                if right not in {p,q}: right = q
                elif left not in {p,q}: left = q

            if (left == p and right == q) or (left == q and right == p):
                if not LCA: LCA = root
                return
            elif right in {p,q}:
                return right
            elif left in {p,q}:
                return left
            else:
                return root
        postorder(root)
        return LCA