# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return

        lvl,ans=[root],[]
        while lvl:
            tmp=[]
            
            for n in lvl:
                tmp.append(n.left)
                tmp.append(n.right)

            ans.append([n.val for n in lvl])    
            lvl = [n for n in tmp if n]
        return ans    