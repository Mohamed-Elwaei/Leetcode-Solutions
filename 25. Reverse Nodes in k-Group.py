# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        order = []
        curr = head
        while curr:
            order.append(curr)
            curr = curr.next
        
        for i in range(0,len(order) - k + 1,k):
            order[i:i+k] = order[i:i+k][::-1]
        
        for i in range(len(order)-1):
            order[i].next = order[i+1]
        
        order[-1].next = None
        return order[0]
        
        
        