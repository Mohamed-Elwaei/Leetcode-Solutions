class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = {0: 1}
        # 1st example is [1,0,1,0,1]
        # prefix sum = {0:1, 1:2, 2:2, 3:1}
        def helper(x):
            if x <= -1:
                return 0
            l, cur = 0, 0
            res = 0
            for r in range(len(nums)):
                cur += nums[r]
                while cur > x:
                    cur -= nums[l]
                    l+=1
                res += (r - l + 1)
            return res
        return helper(goal) - helper(goal - 1)