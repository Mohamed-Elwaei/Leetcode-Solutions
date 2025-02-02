class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums.sort(key = lambda x:abs(x))
        return [n*n for n in nums]