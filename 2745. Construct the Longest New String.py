"""
"AA" is an x-type
'BB' is a y-type.
'AB' is a z-type.

We want to resturn the longest string not containing 'AAA' or 'BBB'

No x-type can be followed by a z-type or another x-type.
No y-type can be followed by a y-type.
No z-type can be followed by a y-type.

We return the longest valid string.

We can start out with any type.

This is a DP problem, the parameters are x,y,z and the last type in the string.
"""

class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        memo = {(0,0,1,'x'):1,(0,0,0,'y'):1 ,(0,0,0,'z'):1}

        def F(x,y,z,t):
            state = (x,y,z,t)
            if state in memo:
                return memo[state]
            
            memo[state] = 1
            if t == 'x':
                if y:
                    memo[state] = max(memo[state], 1 + F(x,y-1,z,'y'))
            
            if t == 'y':
                if x:
                    memo[state] = max(memo[state], 1 + F(x-1,y,z,'x'))
                if z:
                    memo[state] = max(memo[state], 1 + F(x,y,z-1,'z'))
            
            if t == 'z':
                if x:
                    memo[state] = max(memo[state], 1 + F(x-1,y,z,'x'))
                if z:
                    memo[state] = max(memo[state], 1 + F(x,y,z-1,'z'))
            return memo[state]
        
        return max(F(x,y,z-1,'z'), F(x,y-1,z,'y'), F(x-1,y,z,'x')) * 2
