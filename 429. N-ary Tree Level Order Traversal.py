"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root: return root

        ans,level=[],[root]

        while level:
            ans.append([node.val for node in level])
            tmp=[]
            for node in level:
                if node:
                    tmp.extend([c for c in node.children])
            
            level=[node for node in tmp if node]
        return ans