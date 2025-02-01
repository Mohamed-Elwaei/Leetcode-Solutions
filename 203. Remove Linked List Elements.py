# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head==None:return head
        prev=None
        curr=head

        while curr!=None:
            if curr.val==val:
                if not prev:
                    tmp=head
                    head=head.next
                    curr=head
                    del tmp
                    continue
                prev.next=curr.next
                tmp=curr
                curr=prev.next
                del tmp
                continue
            prev=curr
            curr=curr.next
        return head