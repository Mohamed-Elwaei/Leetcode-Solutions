# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        firstHalf, secondHalf = head, slow.next
        slow.next = None
        def dfs(node):
            nonlocal firstHalf
            if not node: return None
            dfs(node.next)
            tmp = firstHalf.next
            firstHalf.next = node
            node.next = tmp
            firstHalf = tmp
        dfs(secondHalf)
        return head
