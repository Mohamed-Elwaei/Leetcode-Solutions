# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev=None
        curr=head
        Sums=None
        newh=Sums
        currSum=0
        while curr!=None:
            currSum+=curr.val
            if curr.val==0:
                if not Sums:
                    Sums=ListNode(val=currSum)
                    newh=Sums
                else:
                    newh.next=(ListNode(val=currSum))
                    newh=newh.next
                # newh.val=currSum
                # newh.next=ListNode(val=0)
                # newh=newh.next
                currSum=0
            tmp=prev
            prev=curr
            curr=curr.next
            del tmp
        tmp=Sums
        Sums=Sums.next
        del tmp
        return Sums