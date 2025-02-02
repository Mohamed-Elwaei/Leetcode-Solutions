class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ret = []
        for i in range(0,n,3):
            if nums[min((i+2),n)] - nums[i] <= k:
                ret.append(nums[i:i+3])
            else:
                return []
        return ret

        