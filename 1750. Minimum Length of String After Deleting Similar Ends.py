
class Solution:
    def minimumLength(self, s: str) -> int:

        l, r = 0, len(s) -1
        while r - l >= 1 and s[l] == s[r]:
            prefix = s[l]
            while l < r and s[l] == prefix:
                l+=1
            suffix = s[r]
            while l<=r and s[r] == suffix:
                r -= 1
        return r - l + 1