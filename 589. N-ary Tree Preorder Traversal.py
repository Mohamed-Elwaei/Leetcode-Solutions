"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def aux(self,root,arr):
        if not root:return 
        arr.append(root.val)
        for c in root.children:
            self.aux(c,arr)
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        arr=[]
        self.aux(root,arr)
        return arr