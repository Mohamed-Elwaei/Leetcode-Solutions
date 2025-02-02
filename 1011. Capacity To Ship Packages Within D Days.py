from math import ceil
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def feasible(capacity) -> bool:
            days = 1
            total = 0
            for weight in weights:
                total += weight
                if total > capacity:  # too heavy, wait for the next day
                    total = weight
                    days += 1
                    if days > D:  # cannot ship within D days
                        return False
            return True
        
        l,r = max(weights), sum(weights)
        while l<=r:
            mid = l + (r - l)//2
            if feasible(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l