# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        string = []
        def preorder(root):
            if not root:
                string.append('N')
            else:
                string.append(f'{root.val}')
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        return ' '.join(string)
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        nodes = data.split()
        self.index = -1
        def preorder():
            self.index += 1
            if nodes[self.index] == 'N':
                return None
            else:

                return TreeNode(int(nodes[self.index]), left = preorder(), right = preorder())
        return preorder()

        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans