class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        nums.sort()
        
        l = 0
        n = len(nums)
        
        for r in range(n):
            if nums[l] != nums[r]:
                l = r
            
            if r - l + 1 > 2:
                return False
        return True