
"""
Let's say that our answer is x where min(bloomDay) <= x <= max(bloomDay).

That means we can make m bouquets if we wait x days.
We can also make them for x+1,x+2,...,max(bloomDay).
But we cannot make them for 0,1,...,x-1 days.

We have a monotinic condition. Which means we can use binary search.
"""


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        def condition(day):
            nonlocal k, m

            bouquets = 0
            size = 0
            for d in bloomDay:
                if d <= day:
                    size += 1
                else:
                    size = 0
                if size == k:
                    bouquets += 1
                    size = 0
            return bouquets >= m

        l,r = min(bloomDay), max(bloomDay)


        while l <= r:
            mid = (r - l) // 2 + l

            if condition(mid):
                r = mid - 1
            else:
                l = mid + 1
        if condition(l):
            return l
        return -1