

import numpy as np
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n==0:
            return 0
        if n==1:
            return 1

        matrix=np.array([[1,1],
                          [1,0]])

        matrix=self.binpow(matrix, n-1)

        return matrix[0][0]


    def binpow(self, matrix, n) :
        if n==0:
            return np.array([[1,0],
                            [0,1]])

        result=self.binpow(matrix, n//2)

        
        x=np.matmul(result,result)
        if n%2:
            x=np.matmul(x,matrix)
        return x     