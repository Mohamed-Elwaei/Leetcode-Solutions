# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        sums = []

        def dfs(root):
            if root==None:
                return 0
            
            sum = 0
            sum = root.val + dfs(root.left) + dfs(root.right)
            sums.append(sum)
            return sum
        dfs(root)
        sums = Counter(sums).most_common()
        freq=[]
        print(sums)
        mostFreq = sums[0][1]

        i=0
        while i<len(sums) and sums[i][1] >= mostFreq:
            freq.append(sums[i][0])
            i+=1
        return freq
        