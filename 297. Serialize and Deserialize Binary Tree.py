# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
   

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        string = []
        def dfs(node):
            if node == None:
                string.append("N")
                return None
            else:
                string.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        for i in range(len(string)):
            if string[i] == float('inf'):
                string[i] = 'N'
            else: string[i] = str(string[i])
        
        return ','.join(string)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        print(data)
        i = [0]
        def dfs():
            if i[0] >= len(data) or data[i[0]] == 'N':
                i[0]+=1
                return None
            else:
                root = TreeNode(val = int(data[i[0]]))
                i[0]+=1
                root.left = dfs()
                root.right = dfs()
                return root
        return dfs()
        
                        
