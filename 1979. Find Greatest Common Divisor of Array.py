class Solution(object):
    # def gcd(self,a,b):
    #     if b==0:
    #         return a,1,0    #GCD, x1, y1

    #     gcd,x1,y1=self.gcd(b,a%b)
    #     x=y1
    #     y=x1-(a//b)*y1
    #     return gcd,x,y
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=max(nums)
        b=min(nums)

        while b>0:
            a,b=b,a%b
        return a
        