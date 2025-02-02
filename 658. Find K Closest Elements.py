import heapq
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        ans=[]
        heap = []

        for n in arr:
            heapq.heappush(heap,(abs(n-x),n))
        for i in range(k):
            tmp=heapq.heappop(heap)
            ans.append(tmp[1])
        return sorted(ans)