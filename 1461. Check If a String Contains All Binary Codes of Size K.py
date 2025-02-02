"""
00 01 11 10

Use a mask, and a rolling hash function.
Store all hashes in a set.

If the sum of all the hashes in the set is equal to 2^(k) - 1, we return true
otherwishe: return false
"""


def solve(s, k):
    mask = 0
    for i in range(k):
        mask |= (1 << i)
    
    S = set()

    h = 0

    for i in range(len(s)):
        h <<= 1
        h |= int(s[i])
        h &= mask

        if i >= k - 1:
            S.add(h)
    
    return len(S) == 2**(k)


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        return solve(s,k)