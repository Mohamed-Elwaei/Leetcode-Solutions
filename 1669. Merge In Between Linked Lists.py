# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr = list1
        firstHalf, secondHalf = None, None
        for i in range(b):
            if i == a - 1:
                firstHalf = curr
            curr = curr.next
        secondHalf = curr.next
        firstHalf.next = list2
        while list2.next: list2 = list2.next
        list2.next = secondHalf
        return list1