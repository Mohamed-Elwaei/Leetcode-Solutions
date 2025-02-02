import heapq
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        #Store the frequencies by descending order: Use a max heap.
        #Iterate over the array:
        #for each iteration:
        # pop from maxheap.
        # if popped element is the same as the last element:
        #   pop another one and insert at the end of the array
        #   add both popped elements back in
        # otherwise:
        #  insert popped element at the end

        counter = {}
        for barcode in barcodes:
            counter[barcode] = counter.get(barcode,0) + 1
        heap = []
        for barcode, frequency in counter.items():
            heapq.heappush(heap, (-frequency, barcode))
        
        for i in range(len(barcodes)):
            freqA, numA = heapq.heappop(heap)
            if i == 0 or numA != barcodes[i - 1]:
                barcodes[i] = numA
                freqA += 1
            else:
                freqB, numB = heapq.heappop(heap)
                barcodes[i] = numB
                freqB += 1
                if freqB != 0:
                    heapq.heappush(heap, (freqB, numB))

            if freqA != 0:
                    heapq.heappush(heap, (freqA, numA))
        return barcodes