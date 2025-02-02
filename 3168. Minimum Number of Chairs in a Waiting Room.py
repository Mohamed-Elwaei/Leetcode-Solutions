class Solution:
    def minimumChairs(self, s: str) -> int:
        
        ans = count = 0
        for c in s:
            if c == 'E': count += 1
            elif c == "L": count -= 1
            ans = max(ans,count)
        return ans