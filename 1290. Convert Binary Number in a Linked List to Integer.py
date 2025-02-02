# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        Value=0
        nums=[]
        tmp=head
        while tmp!=None:
            nums.append(tmp.val)
            tmp=tmp.next
        for i in range(len(nums)-1,-1,-1):
            Value+=(2**(len(nums)-1-i))*nums[i]
        return Value