# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return None
        LT,GT=[],[]

        curr=head
        while curr!=None:
            if curr.val>=x:
                GT.append(curr)
            else:
                LT.append(curr)
            curr=curr.next


        for i in range(1,len(LT)):
            LT[i-1].next=LT[i]
        
        for  i in range(1,len(GT)):
            GT[i-1].next=GT[i]
        
        if LT and LT[-1] and GT and GT[0]:
            LT[-1].next = GT[0]
            GT[-1].next=None
        if LT:
            return LT[0]
        else:
            return GT[0]