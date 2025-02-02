"""
First step is to sort the tasks by increasing enqueueTime, then by duration, then by index.


Then we use a priority queue initialized to the first task.

For each subsequent task:
 if the task ends before or equal to our finishtime:
    append it to the priority queue.
 otherwise we keep processing tasks from our priority queue until the finishtime is more than or equal to the tasks start time.


Our min heap will sort elements by their duration, then their index,

"""

import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [t + [i] for i,t in enumerate(tasks)] #sorted by enqueue time then duration
        tasks.sort()
        print(tasks)

        start,duration,index = tasks[0]
        heap = [] #Min heap

        order = [index]
        finishTime = duration + start

        for t in tasks[1:]:
            
            while heap and t[0] > finishTime:
                duration, index = heapq.heappop(heap)
                finishTime += duration
                order.append(index)
            
            heapq.heappush(heap, (t[1], t[2]))
            finishTime = max(finishTime, t[0])
            
        
        while heap:
            duration,index = heapq.heappop(heap)
            order.append(index)
        return order

