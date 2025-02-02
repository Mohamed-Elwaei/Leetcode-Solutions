class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        """
        1 <= N <= 10^5
        1 <= candidates[i] <= 10^7
        input is a 32 bit integer.

        & is monotinacally decreasing.

        16  10000
        17  10001
        24  11000
        62 111110

        12 001100
        14 001110
        62 111110
        24 011000
        """
        def helper(num):
            for i in range(32):
                if (1 << i) & num:
                    bits[i] += 1
        bits = {i:0 for i in range(32)} #Ith bit to how many numbers have the ith bit set

        for c in candidates:
            helper(c)
        
        return max(bits.values())