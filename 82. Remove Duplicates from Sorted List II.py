# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, left, right = dummy,head,head

        while left:
            while right and right.val == left.val:
                right = right.next
            if right != left.next: #We have a duplicate
                prev.next = right
                left = right
            else:
                prev = left
                left = right
        return dummy.next