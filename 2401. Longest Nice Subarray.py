class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        
        curr = nums[0]
        l = 0

        n = len(nums)
        length = 1
        for r in range(1,n):

            while nums[r] & curr:
                curr = curr ^ nums[l]
                l += 1
            curr ^= nums[r]
            length = max(length, r - l + 1)
        return length