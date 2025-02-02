# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.ans=0
        def search(root):
            if not root: return 0
            curr=root.val
            if curr>=low and curr<=high:
                self.ans+=curr
            if curr<high:
                search(root.right)
            if curr>low:
                search(root.left)
        search(root)
        return self.ans
                