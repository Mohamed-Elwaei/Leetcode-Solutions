class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = {}
        n = len(s)
        l = 0

        ans = 0
        for r in range(n):
            counter[s[r]] = counter.get(s[r],0) + 1

            while counter[s[r]] > 1:
                counter[s[l]] -= 1
                l += 1
            
            ans = max(r - l + 1, ans)
        return ans