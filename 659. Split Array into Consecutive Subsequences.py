
class Solution:
    def isPossible(self, nums: list[int]) -> bool:
        counter = dict()
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        start = next(iter(counter))
        curr = start
        subsequenceLength = 0
        while counter:
            counter[curr] -= 1
            subsequenceLength += 1
            if curr + 1 not in counter: 
                if counter[curr] == 0: 
                    del counter[curr]
                if subsequenceLength < 3: return False
                elif not counter: return True
                else: 
                    curr = next(iter(counter))

            elif counter[curr + 1] > counter[curr]: 
                if counter[curr] == 0: 
                    del counter[curr]
                curr = curr + 1
            elif counter[curr + 1 ]<= counter[curr]:
                subsequenceLength = 0
        return True
s =Solution()
print(s.isPossible(nums = [1,2,3,3,4,5]))