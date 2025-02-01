# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []

        ans,lvl=[],[root]
        flip=False
        while lvl:

            tmp=[]
            for node in lvl:
                tmp.append(node.left)
                tmp.append(node.right)
            if not flip:
               ans.append([node.val for node in lvl])
            else:
               ans.append([node.val for node in lvl[::-1]])
            flip=(flip+1)%2
            lvl=[]
            for node in tmp:
                if node:
                    lvl.append(node)
        return ans