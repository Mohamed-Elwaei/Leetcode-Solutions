# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from collections import defaultdict
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        hmap=defaultdict(lambda :-2)
        index=0
        counter=head
        cycle=True
        while counter!=None and hmap[counter]==-2:
            if hmap[counter]!=-2:
                return hmap[counter]
            hmap[counter]=index
            counter=counter.next
            index+=1
            if counter==None:
                return None
        return counter