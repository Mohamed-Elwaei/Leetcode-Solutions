# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        nodes = []
        curr = head
        stack = []
        while curr:
            nodes.append(curr.val)
            curr = curr.next

        answer = [0] * len(nodes)
        for i in range(len(nodes)-1,-1,-1):
            while stack and stack[-1]<=nodes[i]:
                stack.pop()
            answer[i] = 0 if not stack else stack[-1]
            stack.append(nodes[i])
        return answer        