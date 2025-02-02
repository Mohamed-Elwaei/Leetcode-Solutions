# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def maxI(arr):
            max = [-1,-1]
            for i,n in enumerate(arr):
                print(i,n)
                max = [i,n] if n > max[-1] else max
            return max[0]
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        val = maxI(nums)
        if val==-1:
            return
        root = TreeNode(nums[val],self.constructMaximumBinaryTree(nums[:val]),self.constructMaximumBinaryTree(nums[val+1:]))
        return root

        

        