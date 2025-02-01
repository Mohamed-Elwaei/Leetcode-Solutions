class Solution:
    def myAtoi(self, s: str) -> int:
        
        i = 0
        n = len(s)
        while i < n and s[i] == ' ':
            i+=1
        if i >= n:
            return 0
        sign = 0

        if s[i] == '-':
            i+=1
            sign = 1
        elif s[i] == '+':
            i+=1
        

        ret = 0
        limit = (1 << 31) - 1

        if sign:
            limit += 1

        while i < n and ord('0') <= ord(s[i]) <= ord('9'):
            ret = ret * 10 + (int(s[i]))
            ret = min(limit, ret)
            i+=1
        
        if sign:
            ret = -ret
        return ret
        