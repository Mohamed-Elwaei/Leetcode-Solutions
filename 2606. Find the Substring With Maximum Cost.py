"""

If a substring is negative, do not consider it.

Only consider positive substrings.
"""

class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        mapping = { x:i+1 for i,x in enumerate(string.ascii_lowercase)}
        for c,val in zip(chars,vals):
            mapping[c] = val
            
        
        ans = 0
        
        curr = 0
        
        for c in s:
            curr += mapping[c]
            
            ans = max(curr,ans)
            
            curr = max(0,curr)
        return ans
            