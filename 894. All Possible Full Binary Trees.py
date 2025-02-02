# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        #Return a list of all possible full binary trees with n nodes.
        #Each node should have a value equal to 0.
        #A full binary tree is a binary tree where each node has exactly 0 or 2 children.
        #A full binary tree must have an ODD no. of nodes.
        # 1 <= n <= 20.
        #n = 7.
        #If we decide on a root. the root must have children on both sides or no children at all.
        #If we choose a node at the root,
        #We can have a tree with: 
        #1 on the left, 5 on the right
        #3 on the left, 3 on the right.
        #5 on the left, 1 on the right

        #for a tree with 5 nodes: 1 node as root. 1 node in one side, 3 on the other.
        #for a tree with 3 nodes: 1 node as root, 1 node in one side, 1 on the other.
        #for a tree with 1 nodes: 1 node as root, 1 on the right, 1 on the left
        if n % 2 == 0: return []

        def generate(n):
            if n == 1:
                return [TreeNode()]
            
            ret = []
            for i in range(0, n - 1):
                leftCount = i
                rightCount = n - 1 - i
                if leftCount % 2 == 0 or rightCount % 2 == 0:
                    continue
                leftSubtrees = generate(leftCount)
                rightSubtrees = generate(rightCount)

                for leftSubtree in leftSubtrees:
                    for rightSubtree in rightSubtrees:
                        ret.append(TreeNode(val = 0, left = leftSubtree, right = rightSubtree))
            return ret
        return generate(n)