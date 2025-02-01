"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:return 0
        ans,level=[],[root]
        while level:
            ans.append([n.val for n in level])
            tmp=[]
            for n in level:
                tmp.extend([c for c in n.children])
            level=[n for n in tmp if n]
        return len(ans)