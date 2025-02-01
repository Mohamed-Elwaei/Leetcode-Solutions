# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        if root == None:
            return paths

        
        def dfs(root,path=[]):
            if not root.left and not root.right:
                paths.append(path + [root.val])
                return
            
            if root.left:
                dfs(root.left,path + [root.val])
            if root.right:
                dfs(root.right,path + [root.val])
        dfs(root)
        
        for i,path in enumerate(paths):
            string = ''
            for node in path:
                if string:
                    string+=f'->{node}'
                else:
                    string+=f'{node}'
            paths[i] = string
        return paths

            
        
        
        