# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import collections
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        tmp=headA
        visited=collections.defaultdict(int)
        while tmp!=None:
            visited[tmp]+=1
            tmp=tmp.next
        tmp=headB
        while tmp!=None:
            visited[tmp]+=1
            if visited[tmp]>1:
                return tmp
            tmp=tmp.next    