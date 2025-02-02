from math import ceil,sqrt
class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        factors=[]
        factors2=[]
        for i in range(1,int(sqrt(n))+1):
            if n%i==0:
                factors.append(i)
                factors2.append(n//i)
        if factors2[-1]==factors[-1]:factors2.pop()
        factors.extend(factors2[::-1])
        if k>len(factors):return -1
        else: return factors[k-1]