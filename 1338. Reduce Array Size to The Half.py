from math import ceil
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = dict()
        for n in arr:
            counter[n] = counter.get(n, 0) + 1
        frequencies = sorted(counter.items(), key = lambda x:x[1])
        size = len(arr)
        counter = 0
        curr = 0
        while frequencies and counter  < ceil(size/2):
            counter += frequencies.pop()[1]
            curr += 1
        return curr