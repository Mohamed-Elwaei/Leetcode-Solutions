# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def getLastLevel(root):
            last, currLevel = [], [root]
            while currLevel:
                tmp = []
                for node in currLevel:
                    if node.left:
                        tmp.append(node.left)
                    if node.right:
                        tmp.append(node.right)
                last = [node.val for node in currLevel]
                currLevel = tmp[:]
            return last
        last = getLastLevel(root)
        return last[0] 