"""

nums = [5,8,3]

[5,8,3]
[5,1,3]
[0,1,3] Return False


nums = [4,9,6,10]

[4,9,6,10]
[4,9,6,10]
[4,4,6,10]
[2,4,6,10]


Loop backwards starting from n - 2 where n is the length of our 0-indexed nums array.
We need to get a list of primes to do binary search on them.

for i from n-2 to 0:
    if nums[i+1] > nums[i]: continue

    diff = nums[i] - nums[i+1]

    prime = bs(diff)

    if prime >= nums[i]: return False

    nums[i] -= prime
"""
from typing import List

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:

        primes = []
        max_n = 1001
        sieve = [0] * max_n
        sieve[1] = 1

        i = 2
        while i*i < max_n:
            if sieve[i]:
                i+=1
                continue
            primes.append(i)
            for j in range(i+i, max_n, i):
                sieve[j] = 1
            i += 1
        
        print(primes)
        return 1
    

s = Solution()
print(s.primeSubOperation([]))

