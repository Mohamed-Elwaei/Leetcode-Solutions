"""
Think of the weights as tickets.

If we have n tickets, and an array w = [w1, w2, ... wk]

Then we create an array of intervals.
[[1,w1],[w1+1,w2],[w2+1,w3], ... , [w(k-1) + 1,  wk]].

At each call of pickIndex we generate a random number between [1, sum(w1 + w2 + ... wk)].
call it x.

We do a binary search on the array of intervals to determine at which interval x belongs to.
We then return the index of that interval.

"""
from random import randint

class Solution:

    def __init__(self, w: List[int]):
        total = sum(w)
        intervals = []

        start = 1

        for weight in w:
            intervals.append((start, weight + start - 1))
            start = start + weight 

        self.total = total
        self.intervals = intervals

    def pickIndex(self) -> int:
        total = self.total
        x = randint(1,total)

        index = self.bs(x)
        return index

    def bs(self, x):
        intervals = self.intervals

        l = 0
        r = len(intervals) - 1

        while l <= r:
            mid = (r - l) // 2 + l

            if intervals[mid][0] > x:
                r = mid - 1
            elif intervals[mid][1] < x:
                l = mid + 1
            else:
                return mid
        return l

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()