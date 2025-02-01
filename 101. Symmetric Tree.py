# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def levelOrder(root,reverse=0):
    if not root:
        return []

    ans,lvl = [], [root]

    while lvl:
        tmp = []
        for n in lvl:
            if n:
                tmp.append(n.left)
                tmp.append(n.right)
        
        tmp2=[]
        for n in lvl:
            if n:
                tmp2.append(n.val)
            else:
                tmp2.append(None)
        
        ans.append(tmp2[:])
        lvl = tmp[:]
    if reverse:
        for level in range(len(ans)):
             ans[level].reverse()
    return ans

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        return levelOrder(root.left) == levelOrder(root.right,1)
        