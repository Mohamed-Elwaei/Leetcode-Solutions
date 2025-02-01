# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.st = []
        curr = root
        while curr:
            self.st.append(curr)
            curr = curr.left

    def next(self) -> int:
        ret = self.st.pop()
        curr = ret.right
        while curr:
            self.st.append(curr)
            curr = curr.left
        # print("Next called: stack is ",[n.val for n in self.st])
        return ret.val

    def hasNext(self) -> bool:
        # print("hasNext called, size of stack is: ",len(self.st))
        return len(self.st) >= 1


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()