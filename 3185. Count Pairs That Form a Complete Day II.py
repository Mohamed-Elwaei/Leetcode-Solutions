"""
a mod n = c
b mod n = d

(a + b) mod n = (c + d) mod n

[12,12,30,24,24]

12 mod 24 = 12. find another number that has mod 24 = 12.
30 mod 24 = 6 find another number that has mod 24 = 18.
24 mod 24 = 0 find another number that has mod 24 = 0.


"""

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        
        D = [0] * 24 #D[i] contains how many no.s mod 24 = i.
        
        count = 0
        
        for h in hours:
            rem = h % 24
            
            if rem == 0: # find another no. with remainder = 0 when divided by 24
                count += D[0]
            else: #find another no. with remainder = 24 - rem when divided by 24.
                count += D[24 - rem]
            
            D[rem] += 1
        return count
        