class Solution:
    def isValidSerialization(self, tree: str) -> bool:
        tree = tree.split(',')
        i = 0
        stack = []

        def preorder():
            nonlocal i
            if i >= len(tree):
                return False

            if tree[i] == '#':
                i += 1
                return True

            stack.append(tree[i])
            i += 1
            left = preorder()
            right = preorder()
            stack.pop()

            return left and right

        return preorder() and i == len(tree)