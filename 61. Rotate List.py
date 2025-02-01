# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        if k==0:
            return head
            
        size=0
        tmp=head
        while tmp!=None:
            tmp=tmp.next
            size+=1
        k=k%size    


        tail=head
        while tail.next:
            prev=tail
            tail=tail.next
        
        tail.next=head
        prev.next=None
        head=tail
        return self.rotateRight(head,k-1)