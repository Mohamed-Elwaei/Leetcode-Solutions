"""
Solution: Return longest common prefix
"""
class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        n = min(len(s1), len(s2), len(s3))
        if len({s1[0],s2[0],s3[0]}) != 1:
            return -1
        
        
        i = 0
        while i < n:
            if len({s1[i],s2[i],s3[i]}) != 1:
                break
            i+=1
        
        return (len(s1) - i) + (len(s2) - i) + (len(s3) - i)