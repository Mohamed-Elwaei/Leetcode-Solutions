# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        digits = [0] * 10
        # Odd length palindrome: Only one of the digits is odd
        # Even length palindrom
        self.paths = 0

        def dfs(root):
            if not root:
                return 

            digits[root.val] += 1
            if not root.left and not root.right: # Reached a leaf node
                odds,evens = 0,0
                for digit in digits:
                    if digit%2:
                        odds+=1
                    else:
                        evens+=1
                if sum(digits) % 2 and odds == 1: #Odd length palindrome
                    self.paths+=1
                elif sum(digits) % 2 == 0 and odds == 0:# Even length palindrome
                    self.paths+=1
                
                    
                    
            dfs(root.left)
            dfs(root.right)
            digits[root.val]-=1
        dfs(root)
        return self.paths

