# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorder(self,root,arr):
        if root==None:return
        self.inorder(root.left,arr)
        arr.append(root.val)
        self.inorder(root.right,arr)


    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        A=[]
        self.inorder(root1,A)
        B=[]
        self.inorder(root2,B)
        Combined=[]
        
        while A or B:
            if A and B:
                if A[-1]>B[-1]:
                    Combined.append(A.pop())
                else:
                    Combined.append(B.pop())
            elif not A:
                Combined.append(B.pop())
            elif not B:
                Combined.append(A.pop())
        return Combined[::-1]