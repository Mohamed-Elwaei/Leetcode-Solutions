"""

a mod n = c
b mod n = c

a - b mod n = 0

n | a - b

Use a 'prefix sum'.
nums = [4,5,0,-2,-3,1], k = 5
prefix=[4,9,9, 7, 4, 5]

0 : 2
1 : 
2 : 1
3 : 
4 : 4

count = 1 + 2 + 0 + 3 + 1 = 7
"""


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        dp = [0] * k
        dp[0] = 1
        count = 0

        ps = 0

        for n in nums:
            ps = (ps + n) % k
            count += dp[ps]
            dp[ps] += 1
        
        return count