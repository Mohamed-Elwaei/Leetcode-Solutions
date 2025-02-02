# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        def dfs(root, index):
            if not root:
                return 
            root.val = index
            dfs(root.left, index*2 + 1)
            dfs(root.right, index*2 + 2)

        dfs(root, 0)
        self.root = root

    def find(self, target: int) -> bool:
        directions = []
        tmp = target
        while target > 0:
            if target % 2 == 0: 
                directions.append('right')
            elif target % 2 == 1:
                directions.append('left')
            target = (target - 1) // 2
        curr = self.root
        while directions and curr:
            direction = directions.pop()
            if direction == 'left': curr = curr.left
            elif direction == 'right': curr = curr.right
        return (curr and curr.val == tmp)

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)