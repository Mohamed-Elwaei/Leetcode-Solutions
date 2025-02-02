# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        def preorder(root):
            if not root:
                return '()'
            string = f'({root.val}'
            leftSubtree,rightSubtree = preorder(root.left),preorder(root.right)
            if leftSubtree == '()' and rightSubtree == '()':
                string += ')'
            elif rightSubtree == '()':
                string = string + leftSubtree + ')'
            else:
                string = string + leftSubtree + rightSubtree + ')'
            return string
        return preorder(root)[1:-1:1]