# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def generate(left,right):
            if left == right:
                return [TreeNode(left)]
            if left > right:
                return [None]
            res = []
            for root in range(left,right + 1):
                for leftTree in generate(left, root - 1):
                    for rightTree in generate(root + 1, right):
                        res.append(TreeNode(root,leftTree,rightTree))
            return res
        return generate(1,n)