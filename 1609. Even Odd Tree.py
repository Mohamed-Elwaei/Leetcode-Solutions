# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        def bfs(root):
            tree, level = [],[root]
            while level:
                tmp = []
                for node in level:
                    if node.left:
                        tmp.append(node.left)
                    if node.right:
                        tmp.append(node.right)
                tree.append([node.val for node in level])
                level = tmp[:]
            return tree
        
        tree = bfs(root)
        for i,level in enumerate(tree):
            
            if i%2 == 1: #Odd
                for j in range(len(level) -  1):
                    if level[j]%2 == 1 or level[j] <= level[j + 1]:
                        return False
                if level[-1]%2 == 1:
                    return False
            else: #Even
                for j in range(len(level) - 1):
                    if level[j]%2 == 0 or level[j] >= level[j + 1]:
                        return False
                if level[-1]%2 == 0:
                    return False
        return True
