def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)

class Solution:
    def minOperations(self, A: List[int], B: List[int]) -> int:
        A.sort()
        if len(B) == 1:
            for i in range(len(A)):
                if B[0] % A[i] == 0:
                    return i
            return -1
        

        g = gcd(B[0],B[1])

        for n in B[2:]:
            g = gcd(g,n)
        

        for i in range(len(A)):
            if g % A[i] == 0:
                return i
        return -1