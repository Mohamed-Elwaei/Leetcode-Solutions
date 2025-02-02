"""
hand = [1,2,3,6,2,3,4,7,8], groupSize = 3

hand = [1,2,2,3,3,4,6,7,8]

mapping = {
    1:0,
    2:0,
    3:0,
    4:0,
    6:0,
    7:0
    8:0
}

Solution is : Use a minHeap and extra storage for the hand.

First, map each number to its occurences. 
Second, Insert all the numbers into a minHeap.

Keep popping from the heap untill you reach groupSize.

Add all the numbers back in if there are any left
"""
import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)

        if n % groupSize:
            return False

        counter = {}
        for num in hand:
            counter[num] = counter.get(num, 0) + 1
        
        heap = []
        for num in counter:
            heapq.heappush(heap, num)

        for i in range(n // groupSize):
            group = []
            if groupSize > len(heap):
                return False
            for j in range(groupSize):
                card = heapq.heappop(heap)
                if len(group) == 0 or group[-1] + 1 == card:
                    group.append(card)
                    counter[card] -= 1
                else:
                    return False
            
            for card in group:
                if counter[card] > 0:
                    heapq.heappush(heap, card)
        return True
            




        