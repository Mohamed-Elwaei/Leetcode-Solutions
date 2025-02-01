class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<0:
            return False

        if n & (n-1): # It can only be a power of 4 if only the ith bit is set where i is even.
            return False
        
        for i in range(0,33,2): #Check if the ith bit is even and set
            if (1<<i) & n:
                return True
        return False