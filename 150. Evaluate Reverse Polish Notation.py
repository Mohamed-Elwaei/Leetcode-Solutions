from math import floor

def div(b,a):
    if a<0 and b<0 or a>0 and b>0:
        return floor(a/b)
    else:
        return -floor(abs(a/b))
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        operations = {'+':lambda x,y:x+y,'-':lambda y,x:x-y,'/':div,'*':lambda x,y:x*y}
        for token in tokens:
            if token in '+-/*':
                a,b = nums.pop(),nums.pop()
                nums.append(operations[token](a,b))
            else:
                nums.append(int(token))
        return nums[-1]