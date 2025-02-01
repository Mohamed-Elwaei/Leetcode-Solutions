# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1: return list2
        if not list2: return list1
        if list1.val>=list2.val:
            head=list2
            list2=list2.next
        else:
            head=list1
            list1=list1.next  
        tmp=head       
        while list1 and list2:
            if list1.val>=list2.val:
                tmp.next=list2
                tmp=tmp.next
                list2=list2.next
            else:
                tmp.next=list1
                tmp=tmp.next
                list1=list1.next    
        if list1:tmp.next=list1
        elif list2:tmp.next=list2        
        return head        