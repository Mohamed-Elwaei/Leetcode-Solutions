from collections import deque
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k>0 and stack and stack[-1] > digit:
                stack.pop()
                k-=1
            stack.append(digit)
        for _ in range(k):  stack.pop()
        i = 0
        while i < len(stack) and stack[i]=='0':
            i+=1
        if stack[i:]:
            return ''.join(stack[i:])
        else:
            return '0'