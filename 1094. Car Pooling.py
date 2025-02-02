import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #[[2,1,3],[3,3,7],[4,7,9]]
        # Queue: [2,1,3] capacity = 2
        # Queue: [[2,1,3],[3,3,7]] => [[3,3,7]] capacity = 1
        # Queue: [[3,3,7],[4,7,9]] => [[4,7,9]] capacity = 1

        trips.sort(key = lambda x: (x[1],x[2]))

        queue = []
        for passengers, start, end in trips:
            capacity -= passengers
            while queue and queue[0][0] <= start:
                capacity += -heapq.heappop(queue)[1]
            heapq.heappush(queue, (end, -passengers))
            if capacity < 0: return False
        return True