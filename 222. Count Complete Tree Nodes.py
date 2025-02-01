# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
We can get the depth of the tree in O(log n) time.

We know that the number of nodes in a non-empty tree is 

[2^(depth-1), 2^(depth) - 1]

In a heap the root is 1 left child is 2*i and right is 2*i+1


So we would do a binary search on the range [2^(depth-1)+1, 2^(depth) - 1]

Let's say the first node to not appear is indexed x, then the answer will be x - 1.



Steps:
1. Get the depth of the tree.
2. Do a binary search on the range [2^(depth-1)+1, 2^(depth) - 1]
3. Return x-1 where x is the index of the node to not appear.

"""



class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        #Get the depth of the tree 1-indexed
        def depth(root): 
            if not root:
                return 0
            return 1 + max(depth(root.left), depth(root.right))
        
        #Find if there is a node with index index
        def found(index):
            path = [index]
            while index > 1:
                index //= 2
                path.append(index)
            
            start = 1
            curr = root
            while path:
                nxt = path.pop()
                if start * 2 + 1 == nxt:
                    curr = curr.right
                elif start * 2 == nxt:
                    curr = curr.left
                start = nxt
                
            return curr != None
            
        
        depth = depth(root)
        
        l = 1 << (depth - 1) 
        r = (1 << (depth)) - 1
        
        
        while l <= r:
            mid = (r - l) // 2 + l
            if not found(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l - 1
        
        
        