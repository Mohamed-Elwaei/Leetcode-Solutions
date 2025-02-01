class Solution:
    def reverse(self, x: int) -> int:
        ret = 0
        sign = x < 0

        
        x = abs(x)
        while x>0:
            ret = ret * 10 + (x%10)
            x //= 10

        if sign == 0 and ret > (1 << 31) - 1 or (sign == 1 and ret > (1 << 31)):
            return 0
        
        if sign:
            return -ret
        else:
            return ret