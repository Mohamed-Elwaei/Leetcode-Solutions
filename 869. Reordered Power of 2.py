class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        """
        Brute force (n!) <= 9!
        

        Biggest Digit: 61
        Start with the biggest order. 
        biggest = biggest order
        n = log2(biggest).
        Consider all powers of 2 less than the biggest order.
        If any power of 2 is an anagram of the biggest order, return True.
        """
        def isAnagram(a,b):
            a = [c for c in str(a)]
            b = [c for c in str(b)]
            a.sort()
            b.sort()
            a = ''.join(a)
            b = ''.join(b)
            return a == b
            
        exp = 1
        for _ in range(64):
            if isAnagram(exp, n):
                return True
            exp <<= 1
        return False