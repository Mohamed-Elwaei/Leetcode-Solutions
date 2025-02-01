# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def inorder(root,subroot):
    if not root and not subroot:
        return True
    if not root or not subroot:
        return False
    
    if root.val == subroot.val:
        return inorder(root.left,subroot.left) & inorder(root.right,subroot.right) 
    return False
    



class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if inorder(root,subRoot):
            return True
        
        if not root:
            return False
        
        return self.isSubtree(root.left,subRoot) | self.isSubtree(root.right,subRoot)
        