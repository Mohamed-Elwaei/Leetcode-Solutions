# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        nodes = []
        def inorder(root):
            if not root: return
            inorder(root.left)
            nodes.append(root.val)
            inorder(root.right)
        inorder(root)
        def bst(arr):
            if not arr: return None
            mid = len(arr) // 2
            leftSubtree = bst(arr[:mid])
            rightSubtree = bst(arr[mid + 1:])
            return TreeNode(arr[mid],leftSubtree,rightSubtree)
        return bst(nodes)