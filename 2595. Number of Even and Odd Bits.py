class Solution(object):
    def evenOddBit(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        #       even, odd
        answer=[0,0]


        for i in range(33):
            bit=(n>>i) & 1

            if bit:
                answer[i%2]+=1
        return answer