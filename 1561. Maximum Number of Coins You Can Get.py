import heapq
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        piles = deque(piles)
        score = 0
        while piles:
            alice = piles.pop()
            score += piles.pop()
            bob = piles.popleft()
        return score