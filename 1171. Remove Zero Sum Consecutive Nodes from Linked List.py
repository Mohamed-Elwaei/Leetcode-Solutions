# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prefix = {}
        dummy, sum = ListNode(next = head), 0
        curr = dummy
        while curr:
            sum += curr.val
            prefix[sum] = curr
            curr = curr.next
        
        curr = dummy
        sum = 0
        while curr:
            sum += curr.val
            curr.next = prefix[sum].next
            curr = curr.next
        return dummy.next