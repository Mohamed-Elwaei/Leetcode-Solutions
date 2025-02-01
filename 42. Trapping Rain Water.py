class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        l=0
        r=l+1
        total=0
        finished=False
        callAgain=False
        while not finished:
            currsum=0
            if r>=len(height):break
            while height[r]<height[l]:
                r+=1
                if r==len(height):
                    finished=True
                    r-=1
                    if height[r]<height[l]:
                        tmp2=height[l:r+1]
                        tmp2=tmp2[::-1]
                        return total+self.trap(tmp2)
                    break
            lower=height[l] if height[l]<height[r] else height[r]   
            while l!=r:
                if lower-height[l]>0: currsum+=lower-height[l]   
                l+=1
            total+=currsum    
            if finished: break  
            l=r
            r=l+1     
        return total   


        # while l!=len(height)-1:
        #     currsum=0
        #     while height[r]<height[l]:
        #         r+=1
                
        #     while l<r:
        #         currsum+=height[l]-height[r]
        #         l+=1
        #     total+=currsum
        # return total
       

