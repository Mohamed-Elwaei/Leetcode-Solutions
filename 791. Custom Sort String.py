class Solution:
    def customSortString(self, order: str, s: str) -> str:
        lookup = {}
        for i,c in enumerate(order):
            lookup[c] = i
        
        s = [c for c in s]
        s.sort(key = lambda x: lookup.get(x, -1))
        s = ''.join(s)
        return s