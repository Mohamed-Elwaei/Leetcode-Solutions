# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
We need to know the sum of the left subtree, the right subtree, and the root node.

We also need to know the size of the left and right subtree and the node.
A postorder traversal would be best as the root is traversed last

"""
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        answer = 0

        def F(root): #Returns sum of the nodes of the tree rooted at root and the no. of nodes.
            nonlocal answer
            if root == None:
                return [0,0]
            
            leftSum,leftCount = F(root.left)
            rightSum, rightCount = F(root.right)

            treeSum = leftSum + rightSum + root.val
            treeCount = rightCount + leftCount + 1
            if treeSum // treeCount == root.val:
                answer += 1
            
            return [treeSum, treeCount]
        
        F(root)

        return answer