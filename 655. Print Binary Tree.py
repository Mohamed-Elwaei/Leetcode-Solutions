# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def getHeight(root):
            if not root: return -1
            else:
                return 1 + max(getHeight(root.left),getHeight(root.right))
        height = getHeight(root)
        rows,cols = height + 1, 2**(height + 1) - 1
        matrix = [[''] * cols for _ in range(rows)]
        def dfs(node,l,r,lvl):
            if node == None: return 
            mid = l + (r - l)//2

            matrix[lvl][mid] = str(node.val)
            dfs(node.left,l,mid,lvl + 1)
            dfs(node.right,mid,r,lvl + 1)

        dfs(root,0,cols,0)
        return matrix