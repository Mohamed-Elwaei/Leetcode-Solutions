# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nodes=[]

        curr=head
        if not head:
            return None
        while curr:
            heapq.heappush(nodes, [curr.val,curr])
            curr=curr.next

        order = []

        while nodes:
            order.append(heapq.heappop(nodes)[1])
        
        for i in range(1,len(order)):
            order[i-1].next=order[i]
        
        order[-1].next=None
        return order[0]