class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):

        ans=0
        for i in range(33):
            bit=(n>>i) & 1
            
            if bit:
                ans|=(1<<(32-i-1))
        return ans