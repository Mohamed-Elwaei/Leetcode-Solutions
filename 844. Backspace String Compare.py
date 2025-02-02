"""
Use a stack 

for each charac
    
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        s1 = []
        for c in s:
            if c == '#':
                if s1:
                    s1.pop()
            else:
                s1.append(c)
                
        s2 = []
        for c in t:
            if c == '#':
                if s2:
                    s2.pop()
            else:
                s2.append(c)
        
        while s1 and s2:
            if s1.pop() != s2.pop():
                return False
            
        if len(s1) > 0 or len(s2) > 0:
            return False
        return True