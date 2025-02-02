"""
s is really small ~12.

We could generate all the subsequences of s.

We could have a nested for loop going over each subsequence and making sure that they are disjoint.
Then maximizing the product.

O(2^n * 2^n) = O(2^(2n))
"""

class Solution:
    def maxProduct(self, s: str) -> int:
        
        palis = {} #mask -> length of palindrom
        n = len(s)
        for mask in range(1, 1 << n):
            subsequence = ''

            for i in range(n):
                if (mask >> i) & 1:
                    subsequence += s[i]
            
            if subsequence == subsequence[::-1]:
                palis[mask] = len(subsequence)
        

        answer = 0
        for subsequence_1 in palis:
            for subsequence_2 in palis:
                if subsequence_1 & subsequence_2: continue
                answer = max(palis[subsequence_1] * palis[subsequence_2], answer)
        return answer