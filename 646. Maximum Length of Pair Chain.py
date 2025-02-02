class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[1])
        end = float('-inf')
        chain = 0
        for left, right in pairs:
            if left > end:
                chain += 1
                end = right
        return chain