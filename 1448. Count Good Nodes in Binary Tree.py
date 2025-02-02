# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right




class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count = [0]
        def dfs(root,currMax):
        
            if not root:
                return 
            if root.val>=currMax:
                count[0]+=1
                currMax = root.val
            
            dfs(root.left,currMax)
            dfs(root.right,currMax)

        dfs(root,float('-inf'))
        return count[0]


