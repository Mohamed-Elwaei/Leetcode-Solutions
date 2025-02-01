import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        frequencies = dict()
        for letter in s:
            frequencies[letter] = 1 if letter not in frequencies else  frequencies[letter]+1
        
        queue = []
        for letter,count in frequencies.items():
            heapq.heappush(queue, (-count, letter))
        
        sorted = ""
        while queue:
            count,letter = heapq.heappop(queue)
            sorted += letter * (-count)
        return sorted


        