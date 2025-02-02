"""
Solution:

Iterate over the array from left to right (or vice versa).

count how many 1's occur and add the amount to the answer each time a 0 is encountered.
"""

class Solution:
    def minimumSteps(self, s: str) -> int:
        
        ones = 0
        swaps = 0
        
        for c in s:
            if c == '1':
                ones += 1
            elif c == '0':
                swaps += ones
                
        return swaps