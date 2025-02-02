def F(a, b):
    i = 1
    turn = 0
    while True:
        
        if turn == 0:
            if i > a:
                return i - 1
            a -= i
        else:
            if i > b:
                return i - 1
            b -= i
        i += 1
        turn ^= 1
        
    

class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        
        return max(F(red,blue), F(blue,red))