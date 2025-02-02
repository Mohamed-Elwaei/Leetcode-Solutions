import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        # aaaaabbbbc 5 a 4 b 2 c
        # a        4 a 4 b 2 c
        # ab       4 a 3 b 2 c
        # aba      3 a 3 b 2 c
        # abab     3 a 2 b 2 c
        # ababa    2 a 2 b 2 c
        #Store all the frequencies in a max heap.
        #for i in range(len(s)):
        # pop from max heap
        # if popped is the last element we need to pop another one.
        # put the next element to be popped in.
        # place one or both elements back in the heap after decrementing.

        counter = {} #Letter => occurrences
        for c in s:#Count all occurences for each letter.
            counter[c] = counter.get(c, 0) + 1
        heap = []
        for letter, frequency in counter.items():
            heapq.heappush(heap, (-frequency, letter))
        ret = ''
        for _ in s:
            freqA, letterA = heapq.heappop(heap)
            if not ret or letterA != ret[-1]:
                ret += letterA
                freqA += 1
            elif heap:
                freqB, letterB = heapq.heappop(heap)
                ret += letterB
                freqB += 1
                if freqB != 0:
                    heapq.heappush(heap, (freqB, letterB))
            else: return ''
            if freqA != 0:
                heapq.heappush(heap, (freqA, letterA))
        return ret