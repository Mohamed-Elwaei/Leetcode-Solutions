
from collections import Counter
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        counter = Counter(s)
        st = []
        visited = set()

        for c in s:
            if c in visited:
                counter[c] -= 1
                continue
            while st and st[-1] >= c and counter[st[-1]]:
                visited.remove(st.pop())
            st.append(c)
            counter[c] -= 1
            visited.add(c)
        return ''.join(st)