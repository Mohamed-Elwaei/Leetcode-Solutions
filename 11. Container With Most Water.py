class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        p=0
        q=len(height)-1
        maxArea=0
        for i in range(len(height)):
            side=height[p] if height[p]<height[q] else height[q]
            currArea=side*(q-p)
            maxArea=max(currArea,maxArea)
            if height[p]<height[q]:
                p+=1
            else :q-=1    
        return maxArea