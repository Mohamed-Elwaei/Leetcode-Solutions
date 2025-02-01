class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zeroes = ones = 0
        prefixSum = {0:-1}
        longest = 0
        for i, n in enumerate(nums):
            zeroes += n == 0
            ones += n == 1
            if zeroes - ones not in prefixSum:
                prefixSum[zeroes - ones] = i
            longest = max(longest, i - prefixSum[zeroes - ones])
        return longest