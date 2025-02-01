class TreeNode(object):
    def __init__( self,val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def search(self,root,key):
        tmp=root
        while tmp!=None and tmp.val!=key:
            if key>tmp.val:
                tmp=tmp.right
            else:
                tmp=tmp.left
        return tmp   

    def predecessor(self,node):
        tmp=node.left 
        while tmp.right:
            tmp=tmp.right
        return tmp 

    def successor(self,node):
        tmp=node.right
        while tmp.left:
            tmp=tmp.left
        return tmp
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        node=self.search(root,key)
        if not node:
            return root
        if not node.left and not node.right: #leaf node
            del node
            return root
        
        
        elif node.left: #Swap items with predecessor and delete it
            pre=self.predecessor(node)
            pre.val,node.val=node.val,pre.val
            return self.deleteNode(pre,key)

        else:
            succ=self.successor(node)
            succ.val,node.val=node.val,succ.val
            return self.deleteNode(succ,key)





X = [5,3,6,2,4,None,7]



rootNode=TreeNode(5)
rootNode.left=TreeNode(3)
rootNode.right=TreeNode(6)
rootNode.right.right=TreeNode(7)
rootNode.left.left=TreeNode(2)
rootNode.left.right=TreeNode(4)


rootNode.deleteNode(rootNode,3)

rootNode