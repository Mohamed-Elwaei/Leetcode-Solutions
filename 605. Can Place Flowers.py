class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        ans=0
        if n==0:
            return True
        
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i==0 or flowerbed[i-1]==0) and (i==len(flowerbed)-1 or flowerbed[i+1] == 0):
                ans+=1
                flowerbed[i]=1
                if ans==n:
                    return True
        return False