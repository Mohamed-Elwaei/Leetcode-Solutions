# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
So this looks like a DP problem.

At each node we have two decisions to make: go right or left.

If we decide to go to the right, then we have to know the longest zigzag pattern from the right child starting left.
If we decide to go to the left, then we have to know the longest zigzag pattern from the left child starting right.


Let dfs(node): be a function that returns a 2-tuple of integers.
the first is the longest zigzag pattern by going left from node
the second is the longest zigzag pattern by going right from node


Base case is if we have a null node:
    return -1,-1

We check the longest zigzag pattern going right from the left child
We check the longest zigzag pattern going left from the right child



"""


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        answer = 0

        def dfs(root):
            nonlocal answer
            if root == None:
                return (-1,-1) #longest path starting left and right
            

            leftChild = dfs(root.left)
            rightChild = dfs(root.right)

            ret = (leftChild[1] + 1, rightChild[0] + 1)

            answer = max(answer, ret[0], ret[1])
            return ret
        
        dfs(root)
        return answer