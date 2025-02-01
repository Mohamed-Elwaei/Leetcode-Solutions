"""
(a + bi) * (c + di)

a*c + adi + bci +bdi^2

a*c + adi + bci -bd
a*c - b*d + (ad + bc)i
"""

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a,b = num1.split('+')
        c,d = num2.split('+')
        a,c = int(a),int(c)
        b,d = int(b[:-1]), int(d[:-1])

        return f'{a*c - b*d}+{a*d + b*c}i'