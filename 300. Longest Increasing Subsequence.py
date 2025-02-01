class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        LIS = [1] * n

        for j in range(n-2,-1,-1):
            potentials = []
            for i in range(j+1,n):
                if nums[i]>nums[j]:
                    potentials.append(LIS[i])

            LIS[j] = 1 + max(potentials,default = 0)
        return max(LIS)