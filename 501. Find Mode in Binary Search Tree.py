# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        mode = [0]
        modes = set()
        currMode = [0]
        last = [float('inf')]
        def inorder(root):
            if not root: return None
            inorder(root.left)
            if last[0] != root.val:
                last[0], currMode[0] = root.val, 1
            else:
                last[0], currMode[0] = root.val, currMode[0] + 1
            if currMode[0] == mode[0]:
                modes.add(root.val)
            elif currMode[0] > mode[0]:
                modes.clear()
                modes.add(root.val)
                mode[0] = currMode[0]
            inorder(root.right)
        inorder(root)
        return modes