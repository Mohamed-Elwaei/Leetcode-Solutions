from math import sqrt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        a = 0

        while a*a <= c:
            b2 = c - a*a
            b = int(sqrt(b2))
            if b*b == b2:
                return True
            a+=1
        
        return False

            
