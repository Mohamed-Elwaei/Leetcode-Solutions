class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        """
        2 decisions. Add to the sum or not.
        Dimensions are how many numbers we have.

        We keep track of 3 sums.

        dp = [0,0,0]
        dp[0] = Largest sum such that sum % 3 = 0.
        dp[1] = Largest sum such that sum % 3 = 1.
        dp[2] = Largest sum such that sum % 3 = 2.

        We update accordingly.
        """

        dp = [0] * 3

        for n in nums:
            next = dp[:]
            for i in range(3):
                index = (dp[i] + n) % 3
                next[index] = max(next[index], dp[i] + n)
            dp = next
        return dp[0]