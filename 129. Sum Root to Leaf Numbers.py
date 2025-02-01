# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return
        paths=[]

        def dfs(root,curr):
            curr.append(str(root.val))

            if not root.left and not root.right:
                paths.append(curr[:])
                return 
            
            if root.left:
                dfs(root.left,curr)
                curr.pop()
            if root.right:
                dfs(root.right,curr)
                curr.pop()
            
        dfs(root,[])
        return sum([int(''.join(n)) for n in paths ])