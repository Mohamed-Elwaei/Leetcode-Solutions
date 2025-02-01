class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        nonpositives = 0
        for n in nums:
            nonpositives += n <= 0
        N -= nonpositives
        nums = set(nums)
        for i in range(1,N+1):
            if i not in nums: return i
        return N+1