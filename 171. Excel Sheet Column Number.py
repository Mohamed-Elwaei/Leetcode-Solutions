class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ret=0
        exp=0
        for l in columnTitle[::-1]:
            base=ord(l)-ord('A')+1
            ret+=(26**exp)*base
            exp+=1
        return ret    