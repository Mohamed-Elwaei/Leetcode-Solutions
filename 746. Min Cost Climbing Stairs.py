class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n=len(cost)
        memo={n-1:cost[-1],n-2:cost[-2]}
      
        self.aux(cost,0,memo)
        return min(memo[0],memo[1])
    
    def aux(self,cost,n,memo):

        if n in memo:
            return memo[n]
        if n > len(cost):
            return 0
        memo[n] = cost[n] + min(self.aux(cost,n+1,memo), self.aux(cost,n+2,memo) )

        return memo[n]