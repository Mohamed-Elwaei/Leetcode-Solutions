# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""


In a Binary-search-tree. The left subtree contains values smaller than the root.
and the right subtree contains values more than the root.
Both the left and right subtrees must be BSTs.

Base case:
    if tree is empty:
        return True
    if tree is one node:
        we return True
        
        
We need to make sure, the minimum of the right subtree is greater than the root.
We need to make sure, the maximum of the left subtree is less than the root.

We will return two things, the minimum and maximum of each subtree.
"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        
        answer = True
        def F(root): #F will decide if the nonempty tree at root is a binary search tree.
            nonlocal answer
            if (not root.left) and (not root.right):
                return [root.val, root.val] #Minimum and maximum of the tree.
            
            leftMin, leftMax = [root.val, root.val-1]
            if root.left:
                leftMin, leftMax = F(root.left)
            
            rightMin, rightMax = [root.val + 1, root.val]
            if root.right:
                rightMin, rightMax = F(root.right)
            
            if leftMax >= root.val or rightMin <= root.val:
                answer = False
            
            return [leftMin, rightMax]
        
        F(root)
        
        return answer