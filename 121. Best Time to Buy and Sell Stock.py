class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l=0 #buy
        r=0 #sell
        maximum=0
        while l<=len(prices)-1 and r<=len(prices)-1:
            right=prices[r]
            left=prices[l]
            maximum=max(right-left,maximum)
            if prices[r]<=prices[l]:
                l=r
                r=l+1
                continue
            r+=1
            
        return maximum    