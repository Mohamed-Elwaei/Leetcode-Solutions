import heapq
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = dict() #Count the frequency of each number
        for num in arr:
            counter[num] = counter.get(num,0) + 1
        

        queue = [] #Organize the elements by ascending frequencies
        for num,freq in counter.items():
            heapq.heappush(queue,(freq,num))

        while k>0: #Keep removing elements till k is 0
            freq,num = heapq.heappop(queue)
            if freq > k: #If the frequency 
                return len(queue) + 1
            else:
                k -= freq
        return len(queue)