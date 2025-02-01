"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        level=[root]

        while level:
            tmp=[]
            for n in level:
                tmp.extend([n.left,n.right])
            level=[n for n in tmp if n]
            for i in range(len(level)-1):
                level[i].next=level[i+1]

        return root