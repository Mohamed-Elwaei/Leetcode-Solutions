# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        inordered = []
        def inorder(root):
            if root:
                inorder(root.left)
                inordered.append(root)
                inorder(root.right)
        inorder(root)
        copy = sorted(inordered,key = lambda node: node.val)

        switch = []
        # print([n.val for n in inordered])
        # print([n.val for n in copy])
        for i in range(len(inordered)):
            if inordered[i]!=copy[i]:
                switch.append(inordered[i])
        switch[0].val,switch[1].val = switch[1].val,switch[0].val

        return root






        # stack = (TreeNode(float('-inf')),TreeNode(float('inf')) )
        # found = [False]

        # def inorder(root,stack = stack):
        #     if root==None:
        #         return
            
        #     print(stack[0].val, root.val, stack[1].val,sep=' ')
        #     if not (stack[0].val <= root.val <= stack[1].val):
        #         found[-1] = 1
        #         if root.val >= stack[1].val:
        #             root.val,stack[1].val = stack[1].val,root.val
        #             return
        #         elif root.val <= stack[0].val:
        #             root.val,stack[0].val = stack[0].val,root.val
        #             return 
        #     inorder(root.left, (stack[0],root) )
        #     inorder(root.right, (root,stack[1]))
            
        # inorder(root,stack)
        # return root