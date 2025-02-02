# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        ins = {} #Maps each node to its indegrees. We will use it to find the root
        tree = {} #Map each integer to its node. 

        for parent, child, isLeft in descriptions:
            ins[child] = ins.get(child, 0) + 1
            ins[parent] = ins.get(parent, 0)
            tree[child] = tree.get(child, TreeNode(child))
            tree[parent] = tree.get(parent, TreeNode(parent))

            if isLeft:
                tree[parent].left = tree[child]
            else:
                tree[parent].right = tree[child]
        root = None
        for node in ins:
            if ins[node] == 0:
                root = tree[node]
                break
        return root