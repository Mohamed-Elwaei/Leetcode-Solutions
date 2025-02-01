# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def preorder(self, root, arr):
        if root==None:
            return
        arr.append(root)
        self.preorder(root.left,arr)
        self.preorder(root.right,arr)
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        arr=[]

        self.preorder(root,arr)
        i=1
        while i<len(arr):
            root.right=arr[i]
            root.left=None
            i+=1
            root=root.right
            

        
        