"""
We will loop throught the digits array backward and keep mind of the carry
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        if digits[n-1] != 9:
            digits[n-1] += 1
            return digits
        
        
            
        digits[n-1] = 0
        
        for i in range(n-2,-1,-1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        
        return [1] + digits
        