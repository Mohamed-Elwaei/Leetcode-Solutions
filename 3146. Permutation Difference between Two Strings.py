class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        
        s = {c:i for i,c in enumerate(s)}

        ans = 0

        for i,c in enumerate(t):
            ans += abs(i - s[c])
        
        return ans