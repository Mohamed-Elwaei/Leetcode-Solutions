class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #if a bit has been flipped n times such that n % 3 != 0, then our number contains that bit

        #[2,2,3,2] 2: 10 3: 11

        # [4,1] if a bit has been flipped < 3 times. Our lucky number has that bit set

        #[0,1,0,1,0,1,99] 99: 0b1100011

        #[1,1,0,0,0,1,4] 

        #[2,2,3,2,3,3,1]
        #[6,4]
        def incBits(n):
            for i in range(32):
                currBit = (1 << i) & n
                if currBit:
                    bits[i] += 1
        positives = negatives = 0
        for n in nums:
            positives += n > 0
            negatives += n < 0
            
        bits = [0] * 32
        if negatives % 3 == 0:
            for n in nums:
                if n > 0:
                    incBits(n)
        else:
            for n in nums:
                if n < 0:
                    incBits(abs(n))

        answer = 0
        for i in range(32):
            if bits[i] % 3:
                answer |= (1 << i)
        if negatives % 3:
            answer = -answer
        return answer
        
        