class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1,s2 = [c for c in s1], [c for c in s2]
        s1.sort()
        s2.sort()
        def check(x,y):
            for a,b in zip(x,y):
                if a < b:
                    return False
            return True
        return check(s1,s2) or check(s2,s1)