# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subTrees = {}
        def dfs(node):
            if not node: return '#'
            string =  ','.join([str(node.val),dfs(node.left),dfs(node.right)])
            subTrees[string] = subTrees.get(string,[]) + [node]
            return string
        dfs(root)
        duplicates = []
        for string,trees in subTrees.items():
            if len(trees) > 1:
                duplicates.append(trees[0])
        return duplicates# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subTrees = {}
        def dfs(node):
            if not node: return '#'
            string =  ','.join([str(node.val),dfs(node.left),dfs(node.right)])
            subTrees[string] = subTrees.get(string,[]) + [node]
            return string
        dfs(root)
        duplicates = []
        for string,trees in subTrees.items():
            if len(trees) > 1:
                duplicates.append(trees[0])
        return duplicates