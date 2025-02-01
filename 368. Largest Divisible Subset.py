class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()

        LDS = [[x] for x in nums]
        print (LDS)
        for i in range(len(nums)):
            subproblems = [LDS[k] + [nums[i]] for k in range(i) if nums[i]%nums[k] == 0]
            
            LDS[i] = max(subproblems,key = len,default = [nums[i]])
        return max(LDS,key = len)