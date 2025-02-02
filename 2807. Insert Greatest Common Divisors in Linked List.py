# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def traverse(node):
    if node == None: return 

    traverse(node.next)
    if not node.next: return

    gcdNode = ListNode(val = gcd(node.val, node.next.val), next = node.next)
    node.next = gcdNode





class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        traverse(head)
        return head