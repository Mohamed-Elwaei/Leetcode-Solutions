# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return 
        evens,odds=[],[]

        curr=head
        i=0
        while curr:
            if i:
                odds.append(curr)
            else:
                evens.append(curr)
            curr=curr.next
            i=(i+1)%2
        
        e,o=0,0
        newll=[]
        i=0
        while e<len(evens) and o<len(odds):
            if i:
                newll.append(evens[e])
                e+=1
            else:
                newll.append(odds[o])
                o+=1
            i^=1
        while o <len(odds):
            newll.append(odds[o])
            o+=1
        while e <len(evens):
            newll.append(evens[e])
            e+=1
        
        for i in range(1,len(newll)):
            newll[i-1].next=newll[i]
        
        newll[-1].next=None
        return newll[0]