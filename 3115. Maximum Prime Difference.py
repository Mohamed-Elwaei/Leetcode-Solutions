"""
Solution: abs(i - j) where i is the index of the first occuring prime number and j is the index of the last occuring prime no.
"""
max_n = int((1e5) * 3 + 1)
sieve = [0] * max_n

sieve[1] = 1
for i in range(2,max_n):
    
    if sieve[i]: continue
    
    j = i + i
    while j < max_n:
        sieve[j] = 1
        j += i

def prime(num: int) -> bool:
    return sieve[num] == 0

class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        
        start = end = -1
        n = len(nums)
        for i in range(n):
            if prime(nums[i]):
                start = i
                break
        
        for j in range(n-1,-1,-1):
            if prime(nums[j]):
                end = j
                break
        
        return abs(start - end)