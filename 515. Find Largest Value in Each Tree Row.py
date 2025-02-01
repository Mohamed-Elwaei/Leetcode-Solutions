# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def levelOrder(root):
    if not root:
        return []

    ans,lvl = [], [root]

    while lvl:
        tmp=[]
        for n in lvl:
            if n:
                tmp.extend([n.left,n.right])
        
        ans.append([n.val for n in lvl])
        lvl = [n for n in tmp if n]
    return [max(lvl) for lvl in ans]
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return levelOrder(root)