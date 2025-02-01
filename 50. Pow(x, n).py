class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # negative=False
        # if n<0:
        #     negative=True
        #     n*=-1

        # if n==0:
        #     return 1
        # res=self.myPow(x,n//2)

        # if n%2:
        #     res= res*res*x
        # else:
        #     res= res*res
        # if negative:
        #     return 1/res
        # else:
        #     return res
        
        res=1
        negative=False
        if n<0:
            negative=True
            n*=-1
        while n>0:
            if n%2:
                res*=x
            x*=x
            n//=2
        if negative:
            return 1/res
        else:
            return res