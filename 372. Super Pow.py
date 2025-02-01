class Solution(object):

    def binpow(self,a,b):
        if b==0:
            return 1
        res=self.binpow(a,b//2)
        if b%2:
            return (res*res*a)%1337
        else:
            return (res*res)%1337


    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """

        exp=0
        i=0
        for n in b[::-1]:
            exp+=(10**i)*n
            i+=1
        return self.binpow(a,exp)%1337