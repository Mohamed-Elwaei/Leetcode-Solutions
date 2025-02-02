"""
From each fort, we can move right or left.

So we do two passes, from left to right, and from right to left.

At the first pass, We choose the leftmost fort we occupy, and we move into the rightmost empty fort
At the second pass, We choose the rightmost fort we occupy, and we move into the leftmost empty fort

"""

class Solution:
    def captureForts(self, forts: List[int]) -> int:
        n = len(forts)
        
        source = -1
        dest = -1
        count = answer = 0
        
        for i in range(n):
            if forts[i] == 1:
                source = i
                count = 0
            
            elif forts[i] == 0 and source != -1:
                count += 1
            elif forts[i] == -1:
                answer = max(count, answer)
                source = -1
        
        count = 0
        source = -1
        for i in range(n-1,-1,-1):
            if forts[i] == 1:
                source = i
                count = 0
            elif forts[i] == 0 and source != -1:
                count += 1
            elif forts[i] == -1:
                answer = max(count, answer)
                source = -1
        return answer