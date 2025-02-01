# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        order = []
        def inorder(root):
            if not root:
                return 
            
            inorder(root.left)
            order.append(root.val)
            inorder(root.right)
        inorder(root)
        ans = float('inf')
        for i in range(1,len(order)):
            ans = min(ans, abs(order[i] - order[i-1]))
        return ans