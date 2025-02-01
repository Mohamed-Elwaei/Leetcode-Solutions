class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans=[0] * (n+1)

        def countBits(n):
            bits=0
            while n:
                n&=(n-1)
                bits+=1
            return bits
        for i in range(n+1):
            ans[i] = countBits(i)
        return ans