class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        """
        1 <= N <= 10^5.
        s is lowercase.

        s = 'a b c d e'
             l     r
        answer = 1 + 2 + 3 + 4
        Use the sliding window to get no. of substrings.
        how many unique substrings are present in base.

        s = 'abcdabcd'
        at iteration 3:
        (0,3)
        r = 3 l = 0
        answer = 1 + 2 + 3 + 4

        at iteration 4:
        r = 4 l = 4
        (0,3)
        at iteration 7: (final)
        r = 7 l = 4
        answer = 1 + 2 + 3 + 4 + 1 + 2 + 3 + 4

        Our answer won't be unique. How do we make it unique.
        We could store substrings in a set. It would take a linear memory.
        Store the start and end position of each character.
        """
        N = len(s)

        l = r = 0
        dp = [0] * 26

        while r < N:
            last = ord(s[r]) - ord('a')

            if (r - l) % 26 == (ord(s[r]) - ord(s[l])) % 26:
                dp[last] = max(dp[last], r - l + 1)
                r += 1
            else:
                l = r
        return sum(dp)