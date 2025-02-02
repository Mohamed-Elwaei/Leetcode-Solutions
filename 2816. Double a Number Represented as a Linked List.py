# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""
This is easy to do with O(n) memory using recursion and back-propagation.

But I think we can do it in constant memory using two pointers
"""
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            if curr.val >= 5:
                if prev == None:
                    prev = ListNode(1,curr)
                    head = prev
                else:
                    prev.val += 1
                curr.val = (2 * curr.val) % 10
            else:
                curr.val *= 2
            
            prev = curr
            curr = curr.next
        return head