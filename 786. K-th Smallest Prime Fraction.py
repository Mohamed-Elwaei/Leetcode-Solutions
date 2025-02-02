import heapq
class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """

        fractions = []
        for r in range(len(arr)-1,-1,-1):
            l=0

            while l < r:
                heapq.heappush(fractions, (float(arr[l])/arr[r], [arr[l],arr[r]]))
                l+=1
        

        while k>1:
            (heapq.heappop(fractions))
            k-=1
        
        return heapq.heappop(fractions)[1]