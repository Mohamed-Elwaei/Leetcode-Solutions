# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        
        group = []
        curr = None
        for i in range(1,left+1):
            curr = head if not curr else curr.next
        

        for i in range(right-left+1):
            group.append(curr)
            curr=curr.next
        l,r=0,len(group)-1

        while l<r:
            group[l].val,group[r].val = group[r].val,group[l].val
            l+=1
            r-=1
        
        return head


        