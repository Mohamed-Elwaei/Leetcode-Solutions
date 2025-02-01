# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #First we count the no. of nodes.
        curr = head
        count = 0

        while curr:
            count += 1
            curr = curr.next
        
        target = count - n 
        

        curr = head
        prev = None

        if target == 0:
            tmp = head
            head = head.next
            del tmp
            return head
        
        for _ in range(target):
            prev, curr = curr, curr.next
        
        prev.next = curr.next
        del curr
        return head