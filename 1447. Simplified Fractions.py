"""
A simplified fraction is one where the greatest common divisor of the numerator and denominator is 1.

From 1 to n. Compute all fractions where 1 <= numerator < n and 1 <= denominator <= n and gcd(numerator, denominator) = 1.


For each i from 1 to n, get all coprime pairs (i,j) such that i > j.

"""

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        answer = []
        for denom in range(1, n+1):
            for numer in range(1, denom):
                if gcd(numer, denom) == 1:
                    answer.append(f'{numer}/{denom}')
        return answer