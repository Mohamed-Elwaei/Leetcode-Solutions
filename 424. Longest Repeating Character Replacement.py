

def F(s,k,letter):
    n = len(s)
    l = 0
    ans = 0
    for r in range(n):
        if s[r] != letter:
            k-=1

        while k < 0:
            if s[l] != letter:
                k += 1
            l += 1
        ans = max(ans, r - l + 1)
    return ans
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        ans = 0
        for c in string.ascii_uppercase:
            ans = max(ans, F(s,k,c))
        return ans