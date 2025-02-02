# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
We traverse the tree.

We then have some cases to deal with.

Case 1: the node we are currently at has to be deleted
Case 2: the node we are currently at does not have to be deleted, but is a parent of a node that has to be deleted.
Case 3: the node we are currently at does not have to be deleted, and is not a parent of a node that has to be deleted.


To deal with case 1. We consider the children of the node as the new roots
To deal with case 2. We declare the left or right child to be null, before traversing the left and right subtree.

"""

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        S = set([root])
        to_delete = set(to_delete)
        def dfs(root):
            if root == None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            if left == 1:
                root.left = None
            if right == 1:
                root.right = None
            
            ret = 0
            if root.val in to_delete:
                ret = 1
                if root.left:
                    S.add(root.left)
                if root.right:
                    S.add(root.right)
                if root in S:
                    S.remove(root)
            return ret
        dfs(root)
        return list(S)