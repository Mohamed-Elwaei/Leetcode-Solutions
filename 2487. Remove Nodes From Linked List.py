# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        def traverse(head):
            if not head:    return
            arr.append(head)
            traverse(head.next)
        traverse(head)
        stack = []
        for i in range(len(arr)-1,-1,-1):
            node = arr[i]
            while stack and stack[-1].val <= node.val:
                stack.pop()
            arr[i] = None if stack else node
            stack.append(node)
        
        i = 0
        newHead = len(arr)
        while i<len(arr):
            j = i + 1
            while j<len(arr) and arr[j]==None:
                j+=1
            if arr[i]:
                newHead = min(i,newHead)
                arr[i].next = arr[j] if j<len(arr) else None
            i = j
        return arr[newHead]

            