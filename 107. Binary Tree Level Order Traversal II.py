# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return root
        ans,level=[],[root]

        while level:
            ans.append([n.val for n in level[::-1]])
            tmp=[]
            for n in level:
                tmp.extend([n.right,n.left])
            level=[n for n in tmp if n]
        
        return ans[::-1]