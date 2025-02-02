class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        Max=max(candies)
        ans=[0] * len(candies)

        for i, num in enumerate(candies):
            if num + extraCandies >= Max:
                ans[i] = 1
        return ans