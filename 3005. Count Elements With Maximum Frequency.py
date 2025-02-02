from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        frequencies = dict()
        
        for n in nums:
            frequencies[n] = frequencies.get(n,0) + 1
        
        order = list(frequencies.items())
        
        order.sort(key = lambda x: x[1], reverse = True)
        
        
        maxFreq = order[0][1]
        
        ans = maxFreq
        
        for i in range(1, len(order)):
            if order[i][1] != maxFreq: return ans
            ans += order[i][1]
        
        return ans