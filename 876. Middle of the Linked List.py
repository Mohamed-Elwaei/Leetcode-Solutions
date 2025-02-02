# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import ceil
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle = head
        count = 0
        def dfs(node, index = 0):
            nonlocal middle, count
            if not node:
                return
            count = index
            dfs(node.next, index + 1)
            if index == ceil(count / 2):
                middle = node
        dfs(head)
        return middle