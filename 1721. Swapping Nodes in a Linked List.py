# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        size=0
        curr=head
        while curr:
            if size==k-1:
                first=curr
            size+=1
            curr=curr.next
        Second=head
        for _ in range(size-k):
            Second=Second.next
        Second.val,first.val=first.val,Second.val
        return head
        
        