class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        total,res = 0,-1
        for n in nums:
            if total > n:
                res = total + n
            total+=n
        return res