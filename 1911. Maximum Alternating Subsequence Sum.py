class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        score = turn = 0
        evens = []
        odds = []
        while len(nums) >= 2 and nums[-1] == nums[-2]:
            nums.pop()
        for n in nums:
            if turn == 0: # Looking for an even index
                if not evens:
                    evens.append(n)
                elif evens[-1] < n:
                    evens[-1] = n
                elif evens[-1] >= n:
                    odds.append(n)
                    turn ^= 1
            elif turn == 1: # Looking for an odd index
                if not odds:
                    odds.append(n)
                elif odds[-1] > n:
                    odds[-1] = n
                elif odds[-1] <= n:
                    evens.append(n)
                    turn ^= 1
        for n in nums[::-1]:
            if odds and n == odds[-1]:
                odds.pop()
                break
            elif n == evens[-1]:
                break
        return sum(evens) - sum(odds)

