class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """

        xor=start^goal #get the no. of bits that are different

        count=0
        while xor!=0:
            xor=xor&(xor-1) #clear the rightmost bit until xor is 0
            count+=1
        return count