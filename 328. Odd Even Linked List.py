# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        


        def dfs(head, index):  
            if not head:
                return [None,None]
            odd, even = dfs(head.next, index + 1)
            if index % 2 == 1:
                head.next = odd
                odd = head
            else:
                head.next = even
                even = head
            return odd, even
        odd, even = dfs(head, 1)
        curr = odd
        while curr and curr.next:
            curr = curr.next
        if curr:
            curr.next = even
        return head