class Node:
    def __init__(self,val,next = None):
        self.val,self.next = val, next
class MyLinkedList:

    def __init__(self):
        self.head = None
    def get(self, index: int) -> int:
        curr = self.head
        while curr!= None and index > 0:
            curr,index = curr.next, index - 1
        if not curr: return -1
        return curr.val

    def addAtHead(self, val: int) -> None:
        node = Node(val,self.head)
        self.head = node
        
    def addAtTail(self, val: int) -> None: 
        if not self.head: 
            self.addAtHead(val)
            return    
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(val,None)

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0: return self.addAtHead(val)
        curr = self.head
        before = None
        while curr!=None and index>0:
            before,curr = curr,curr.next
            index -= 1
        if curr == None and index > 0: return None
        elif curr == None and index == 0: return self.addAtTail(val)
        else:
            node = Node(val,curr)
            before.next = node


    def deleteAtIndex(self, index: int) -> None:
        if not self.head: return
        if index == 0: 
            tmp = self.head
            self.head = self.head.next
            del tmp
            return
        before,curr = None, self.head
        while curr != None and index > 0:
            before,curr = curr, curr.next
            index -= 1
        if curr == None and index >= 0: return
        else:
            before.next = curr.next
            del curr


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)