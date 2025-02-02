from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        ans = r
        while l <= r:
            k = l + (r - l) // 2
            print(k)
            hours = 0
            for pile in piles:
                hours += ceil(pile / k)
            if hours <= h:
                ans = min(ans,k)
                r = k - 1
            else:
                l = k + 1

        return ans