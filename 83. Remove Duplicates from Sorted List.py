# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev=head
        if not prev:
            return None
        curr=prev.next
        if not curr:
            return prev
        while curr:
            if curr.val==prev.val:
                prev.next=curr.next
                del curr
                curr=prev.next
                continue
            prev=curr
            curr=prev.next
        return head