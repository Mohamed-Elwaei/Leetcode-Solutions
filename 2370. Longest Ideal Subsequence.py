"""
s is long, but each s[i] has a range of only 26.
0 <= k <= 25.

A good strategy would be use a hashMap of size 26.

Each key is a letter and the values are the longest subsequence ending with the letter.

for each character x:

    for each character y:
        check the absolute difference of the two is less than or equal to k:
        If it is:
            mapping[x] = max(mapping[x] ,mapping[y] + 1)


Time complexity would bs O(n * k).
Memory complexity would be O(26)
"""

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        mapping = {c:0 for c in string.ascii_lowercase}

        for x in s:
            mapping[x] += 1
            for i in range(max(ord('a'), ord(x) - k), min(ord('z') + 1, ord(x) + k + 1)):
                y = chr(i)
                if x == y: 
                    continue
                if abs(ord(y) - ord(x)) <= k:
                    mapping[x] = max(mapping[x], mapping[y] + 1)
         
        return max(mapping.values())