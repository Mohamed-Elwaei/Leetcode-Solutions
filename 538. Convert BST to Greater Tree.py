# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        nodes=[]
        
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            nodes.append(root)
            inorder(root.right)
        inorder(root)
        sums = [0 for i in nodes]
        sum = 0
        for i in range(len(nodes)-1,-1,-1):
            sums[i] += nodes[i].val + sum
            sum+=nodes[i].val
            
        for i in range(len(nodes)):
            nodes[i].val = sums[i]
        
        
        return root
        

        