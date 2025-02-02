"""
s = "1101" : 13
s = "1110" : 14
s = "0111" : 7
s = "1000" : 8
s = "0100" : 4
s = "0010" : 2
s = "0001" : 1
"""


def increment(s):
    num = [int(i) for i in s]

    num = num[::-1]
    ret = []
    carry = 1
    for i in range(len(num)):
        ret.append(carry ^ num[i])
        carry = carry & num[i]
    if carry:
        ret.append(carry)
    
    ret = ret[::-1]
    ret = [str(i) for i in ret]
    ret = ''.join(ret)
    return ret

class Solution:
    def numSteps(self, s: str) -> int:
        count = 0


        while s != '1':
            if s[-1] == '1':
                s = increment(s)
            else:
                s = s[:-1]
            count += 1
        return count