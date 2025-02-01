# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        first=head
        second=first.next
        if not second:return first
        third=second.next
        first.next=None
        if not third:
            second.next=first
            return second
        while third:
            second.next=first
            first=second
            second=third
            third=second.next
        second.next=first    
        return second    