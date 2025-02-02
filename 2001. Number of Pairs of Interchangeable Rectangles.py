
"""
nC2 is equal to number of pairs we have from n elements.

nC2 = n!/((n-2)!*2) = (n * (n-1) * (n-2)!) / (2 * (n-2)!) = (n*(n-1))/2


so if we have n elements that are interchangeable with each other, we can use this formula quickly.


If we convert them to floating points, we might lose precision.
So we will divide the width and heigh of each rectangle by their greatest common divisor.
After dividing we will get a pair of irreducible fractions, written as pairs.
We will use a hashmap.
"""
from collections import defaultdict

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        
        hashmap = defaultdict(int)
        for a,b in rectangles:
            num = a // gcd(a,b)
            den = b // gcd(a,b)

            hashmap[(num,den)]+=1

        
        answer = 0
        for val in hashmap.values():
            answer += (val * (val - 1)) // 2
        
        return answer