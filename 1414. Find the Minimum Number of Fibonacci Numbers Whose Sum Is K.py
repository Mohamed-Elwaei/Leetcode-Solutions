class Solution(object):

    def fibs(self,k):
        nums=[0,1]
        a,b=0,1
        while nums[-1]<k:
            tmp=a+b
            a=b
            b=tmp
            nums.append(b)
        return nums
    def findMinFibonacciNumbers(self, k):
        """
        :type k: int
        :rtype: int
        """

        fibs=self.fibs(k)
        ans=0
        for i in fibs[::-1]:
            if k==0:
                return ans
            if i<=k:
                k-=i
                ans+=1
        
        return ans