"""
Map each character in t to its frequency.

Then we will use the sliding approach.

We will also map each character in window to its frequency in the window.

If we have excess characters, we will try to shrink the window from the left
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def valid():
            for c in string.ascii_lowercase:
                if mapping[c] > window[c]:
                    return False
            for c in string.ascii_uppercase:
                if mapping[c] > window[c]:
                    return False
            return True
        
        
        window = {c:0 for c in string.ascii_lowercase}
        mapping = {c:0 for c in string.ascii_lowercase}
        for c in string.ascii_uppercase:
            window[c] = 0
            mapping[c] = 0
            
        for c in t:
            mapping[c] += 1
            
        
        l = 0
        n = len(s)
        ret = ''
        for r in range(n):
            window[s[r]] += 1
            
            while l <= r and window[s[l]] > mapping[s[l]]:
                window[s[l]] -= 1
                l += 1
            
            if valid():
                if ret == '' or len(ret) > r - l + 1:
                    ret = s[l:r+1]
        return ret
                