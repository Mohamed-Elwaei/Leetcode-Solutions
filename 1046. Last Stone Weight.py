import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        heap = []
        for stone in stones:
            heapq.heappush(heap,-stone)


        while len(heap)>1:
            a,b = -heapq.heappop(heap),-heapq.heappop(heap)

            if a==b:
                continue
            else:
                heapq.heappush(heap,-abs(a-b))
        if heap:
            return -heap[0]
        return 0