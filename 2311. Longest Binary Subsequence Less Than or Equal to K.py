class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        val = 0
        cnt = 0
        pow = 1

        for i in range(len(s) - 1, -1, -1):
            if val + pow <= k:
                if s[i] == '1':
                    cnt += 1
                    val += pow
                pow <<= 1

        return s.count('0') + cnt