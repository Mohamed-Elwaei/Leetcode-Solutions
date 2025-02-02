from collections import deque
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums = set([int(x,base = 2) for x in nums])
        curr = 0
        while curr in nums:
            curr+=1
        
        curr = bin(curr)[2:]
        curr = deque([b for b in curr])

        while len(curr) < len(nums):
            curr.appendleft('0')
        curr = ''.join(curr)
        return curr