# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def bfs(root):
    ans,lvl = [],[root]
    while lvl:
        tmp = []
        for node in lvl:
            tmp.append(node.left)
            tmp.append(node.right)
        
        ans.append(lvl[:])
        lvl = [node for node in tmp if node]
    return ans

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth ==1:
            node = TreeNode(val)
            node.left = root
            return node
        depth-=1

        levels = bfs(root)

        for node in levels[depth-1]:

            tmp = TreeNode(val)
            tmp.left = node.left
            node.left = tmp
            tmp = TreeNode(val)
            tmp.right = node.right
            node.right = tmp
        return root