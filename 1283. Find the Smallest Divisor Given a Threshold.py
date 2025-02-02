from math import ceil
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def condition(mid):
            ans = 0
            for n in nums:
                ans += ceil(n / mid)
            return ans <= threshold # Divisor is satisfactory

        total = sum(nums)
        l,r = 1, total
        while l<=r:
            mid = l + (r - l) // 2
            if condition(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
