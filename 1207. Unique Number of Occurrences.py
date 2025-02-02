class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = dict()
        for n in arr:
            if n in counter:
                counter[n] +=1
            else:
                counter[n] = 1
        frequencies = set()
        for n in counter:
            if counter[n] in frequencies:
                return False
            frequencies.add(counter[n])
        return True