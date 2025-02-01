class Solution:
    def numTrees(self, n: int) -> int:
        trees = [0] * (n + 1)
        trees[0] = trees[1] = 1

        for t in range(2,n + 1):
            for root in range(t):
                left = trees[root]
                right = trees[t - root - 1]
                trees[t] += right * left
        return trees[-1]