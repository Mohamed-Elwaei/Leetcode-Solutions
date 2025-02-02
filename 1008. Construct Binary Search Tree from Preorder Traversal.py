# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        stack = []
        i = [0]
        def dfs(i):
            if stack and stack[-1] < preorder[i[0]]:
                stack.pop()
                return None

            node = TreeNode( preorder[i[0]])
            stack.append(preorder[i[0]])
            i[0] += 1
            if i[0] < len(preorder):
                node.left = dfs(i)
            if i[0] < len(preorder):
                node.right = dfs(i)
            return node
        root = dfs(i)
        return root