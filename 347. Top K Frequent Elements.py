import heapq
from collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq=defaultdict(int)
        for n in nums:
            freq[n]+=1
        
        
        ret = []

        for n in freq:
            ret.append((freq[n],n))
        ret=sorted(ret,reverse=True)
        print(ret)
        ret=[x[1] for x in ret[:k]]

        return ret
        