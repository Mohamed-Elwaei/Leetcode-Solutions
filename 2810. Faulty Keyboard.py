from collections import deque
class Solution:
    def finalString(self, s: str) -> str:
        
        partition = deque([])
        
        r = 0
        ret = ''
        for r in range(len(s)):
            if s[r] == 'i':
                ret = ret[::-1]
            else:
                ret += s[r]
        return ret