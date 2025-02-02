# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
We do a level order traversal (breadth-first search for a tree).
"""
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        

        currLvl = 1
        maxSum = root.val
        ans = 1
        queue = deque([root])
        while queue:
            nxtLevel = []
            currSum = 0

            for _ in range(len(queue)):
                node = queue.popleft()
                currSum += node.val

                if node.left:
                    nxtLevel.append(node.left)
                if node.right:
                    nxtLevel.append(node.right)
            
            if currSum > maxSum:
                maxSum = currSum
                ans = currLvl

            queue.extend(nxtLevel)
            currLvl += 1
        
        return ans