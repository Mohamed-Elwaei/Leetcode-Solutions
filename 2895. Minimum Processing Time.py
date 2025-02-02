"""
Each core in a processor can be used again only when all other cores are empty.


Let's sort the tasks array.

We can assign the last task with the last four tasks. Greedy choice.

So first processor available will get the longest four tasks. The second processor gets the second longest 4 and so on.
"""

import heapq
class Solution:
    def minProcessingTime(self, P: List[int], T: List[int]) -> int:
        heap = P
        heapq.heapify(heap)
        T.sort()
        
        ans = 0
        
        while T:
            taskTime = T[-1]
            for _ in range(4):
                T.pop()
            
            timeAvailable = heapq.heappop(heap)
            
            ans = max(ans, timeAvailable + taskTime)
            
        return ans
            
            