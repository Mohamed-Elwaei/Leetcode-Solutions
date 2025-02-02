"""
First step is to hash each number to its frequencies and then sort the pairs of numbers and their frequencies.

nums = [2,2,3,3,3,4]


nums = [(2,2),(3,3),(4,1)]

One thing to notice the order does not matter

counter[i][1] = maximum score for counter[0..i]
"""

class Solution:
    
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = {}
        for n in nums:
            counter[n] = counter.get(n,0) + 1
        
        counter = [[num,freq*num] for num,freq in counter.items()]
        counter.sort()

        for i in range(1,len(counter)):
            if counter[i-1][0] + 1 < counter[i][0]:
                counter[i][1] += counter[i-1][1]
            else:
                if i == 1:
                    counter[i][1] = max(counter[i][1], counter[i-1][1])
                else:
                    counter[i][1] = max(counter[i][1] + counter[i-2][1], counter[i-1][1])
        return counter[-1][-1]
