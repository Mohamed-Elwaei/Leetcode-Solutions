class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        st = 0
        for c in s:
            if c == '(': st += 1
            elif c == ')':
                if st: st -= 1
                else:
                    count += 1
        count += st
        return count