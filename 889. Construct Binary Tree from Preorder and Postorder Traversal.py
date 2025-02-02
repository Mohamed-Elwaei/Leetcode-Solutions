# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructFromPrePost(self, pre: list[int], post: list[int]):
        """
        In pre: root is at the beginning.
        In post: root is at the end.
        pre = [1,2,4,5,3,6,7]
        post = [4,5,2,6,7,3,1]
        
        root = pre[0] = post[last]
        left Child is pre[1]
        right Child is post[last - 1]




        root = 1
        pre = [1,2,4,5,3,6,7]
        post = [4,5,2,6,7,3,1]

        root = 2
        pre = [2,4,5,3,6,7]
        post = [4,5,2]

        root = 4
        pre = [4,5,3,6,7]
        post = []
        
        root = 5
        pre = [5,3,6,7]
        post = [4,5]

        root = 3
        pre = [3,6,7]
        post = [4,5,2,6,7,3]

        root = 6
        pre = [6,7]
        post = [4,6,2,6]

        root = 7
        pre = [7]
        """

        def index(arr,target):
            x = -1
            for i in range(len(arr)):
                if arr[i] == target:
                    return i
            return -1

            
        def dfs(pre, post):
            if not pre or not post:
                return None
            
            root = TreeNode(pre[0])
            leftVal = -1 if len(pre) == 1 else pre[1]
            rightVal = -1 if len(post) == 1 else post[-2]

            tmp = index(post,leftVal)
            if tmp != -1:
                root.left = dfs(pre[1:], post[:tmp + 1])
            
            tmp = index(pre, rightVal)
            if tmp != -1:
                root.right = dfs(pre[tmp:], post[:-1])
            return root
        return dfs(pre, post)

s = Solution()
s.constructFromPrePost(preorder = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1])