class Solution:
    def maxDepth(self, s: str) -> int:
        #depth('') = 0
        #depth(C) = 0 where c is a single charater
        #depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's.
        #depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
        st = []
        ans = 0
        for c in s:
            if c == '(': st.append(c)
            elif c == ')': st.pop()
            ans = max(ans, len(st))
        return ans