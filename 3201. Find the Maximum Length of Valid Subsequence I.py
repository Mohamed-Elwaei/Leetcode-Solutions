"""
2 cases:

1. subsequence has (sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2 == 0.
2. subsequence has (sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2 == 1.


Case 1 can happen if and only if the subsequence is all odd numbers or all even numbers.
Case 2 can happen if and only if the subsequence has every even number has an odd number before and after it and vice versa.


We do 4 iteration.

All even subsequence.
All odd subsequence.
2 subsequences for case 2.

"""

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        
        AllOdds = 0
        AllEvens = 0
        EvenOdd = 0
        OddEven = 0
        
        flagEvenOdd = 0
        flagOddEven = 0
        for n in nums:
            if n&1: #Odd no.
                AllOdds += 1
                if flagOddEven == 0:
                    OddEven += 1
                    flagOddEven = 1
                
                if flagEvenOdd == 1:
                    EvenOdd += 1
                    flagEvenOdd = 0
            elif n&1 == 0: #Even No.
                AllEvens += 1
                
                if flagOddEven == 1:
                    OddEven += 1
                    flagOddEven = 0
                
                if flagEvenOdd == 0:
                    EvenOdd += 1
                    flagEvenOdd = 1
        return max(EvenOdd, OddEven, AllOdds, AllEvens)
        