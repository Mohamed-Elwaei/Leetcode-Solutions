class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        #Valid Parentheses:
        #Empty Strings
        #AB where A is valid and B is valid
        #(A) where A is valid

        #opens = [], closed = []
        #"lee(t(c)o)de)"
        st = []
        toRemove = set()
        for i in range(len(s)):
            if s[i] == '(':
                st.append(i)
            elif s[i] == ')':
                if not st:
                    toRemove.add(i)
                else:
                    st.pop()
        for i in st:
            toRemove.add(i)
        ret = ''
        for i in range(len(s)):
            if i not in toRemove:
                ret += s[i]
        return ret