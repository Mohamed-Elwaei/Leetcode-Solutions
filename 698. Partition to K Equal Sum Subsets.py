class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        """
        [1,2,3,4] k = 2, target = 5
        [2,3,4] k =2, target = 3
        [2,4] k = 2, target = 0


        """

        memo = {}
        total = sum(nums)
        if total // k != total / k: return False
        target = total // k
        def dfs(picked,k,rem):
            state = (picked,k,rem)
            if state in memo:
                return memo[state]
            if k == 0:
                return True
            elif rem == 0:
                memo[state] = dfs(picked,k - 1,target)
                return memo[state]

            memo[state] = False
            for i in range(len(nums)):
                if picked & (1 << i):
                    continue
                else:
                    if rem - nums[i] >= 0 and dfs(picked | (1 << i), k, rem - nums[i]):
                        memo[state] = True
                        return True
            return memo[state]
        return dfs(0, k, target)