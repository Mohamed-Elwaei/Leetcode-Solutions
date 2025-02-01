# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Node:
    def __init__(self,val=0,left=None,right=None,bf=0,height=0):
        self.val=val
        self.left=left
        self.right=right
        self.bf=bf
        self.height=height




class TreeNode(Node):
    def __init__(self,root=None):
        self.root=root

    def __update(self,node):
        lh= -1 if not node.left else node.left.height
        rh= -1 if not node.right else node.right.height

        node.height=1+max(lh,rh)
        node.bf=rh-lh

    
    def __rightRotate(self,node):
        New_P=node.left
        node.left=New_P.right
        New_P.right=node
        self.__update(node)
        self.__update(New_P)
        return New_P

    def __leftRotate(self,node):
        New_P=node.right
        node.right=New_P.left
        New_P.left=node
        self.__update(node)
        self.__update(New_P)
        return New_P



    def insert(self,val):
        self.root=self.__insert(self.root,val)

    def __insert(self,root,val):

        if root==None:
            return Node(val)
        
        elif root.val==val:
            return None
        
        elif root.val<val:
            root.right=self.__insert(root.right,val)
       
        elif root.val>val:
            root.left=self.__insert(root.left,val)

        self.__update(root)

        return self.__balance(root)
    
    def __balance(self,node):
        #Left Heavy
        if node.bf==-2:
            #Left left case
            if node.left.bf<=0:
                return self.__rightRotate(node)
            #Left right case
            else:
                return self.__leftRightCase(node)
        #Right Heavy
        elif node.bf==2:
            if node.right.bf>=0:
                return self.__leftRotate(node)
            else:
                return self.__rightLeftCase(node)
        return node
    

    def __leftRightCase(self,node):
        node.left=self.__leftRotate(node.left)
        
        return self.__rightRotate(node)

    def __rightLeftCase(self,node):
        node.right=self.__rightRotate(node.right)

        return self.__leftRotate(node)
    



class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        
        avl=TreeNode()

        while head!=None:
            avl.insert(head.val)
            head=head.next
        return avl.root

        
