# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        def bfs(root):
            ans,lvl = [],[root]

            while lvl:
                tmp = []
                for node in lvl:
                    tmp.extend([node.left,node.right])
                ans.append([node.val for node in lvl])
                lvl = [node for node in tmp if node]
            return ans
        levels = bfs(root)
        return [float(sum(level)/len(level)) for level in levels]        