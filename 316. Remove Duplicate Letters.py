from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        st = []
        visited = set()
        counter = Counter(s)
        for c in s:
            if c in visited: 
                counter[c] -= 1
                continue
            while st and st[-1] >= c and counter[st[-1]]:
                visited.remove(st.pop())
            st.append(c)  
            visited.add(c)
            counter[c] -= 1
        return ''.join(st)