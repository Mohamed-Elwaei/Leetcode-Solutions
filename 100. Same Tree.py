# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def levelorder(root):
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
        lvl = tmp
    return ans
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        treep=levelorder(p)
        treeq=levelorder(q)
        return treep == treeq
        
        
        