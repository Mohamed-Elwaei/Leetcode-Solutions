class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def countBits(n):
            bits = 0
            while n>0:
                bits += n & 1
                n = (n>>1)

            return bits
        return countBits(n) == 1