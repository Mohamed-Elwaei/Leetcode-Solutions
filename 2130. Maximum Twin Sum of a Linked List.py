# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import defaultdict
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        hmap=defaultdict(ListNode)
        tmp=head
        size=0
        maxSum=0
        while tmp!=None:
            hmap[size]=tmp
            size+=1
            tmp=tmp.next
            
        for i in range((size+1)//2):
            first=hmap[i].val
            second=hmap[size-1-i].val
            maxSum=max(maxSum,first+second)
        return maxSum 