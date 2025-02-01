class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        #[5,4,0,3,1,6,2] 
        #s = [nums[0],nums[5],nums[6],nums[2]] => [5,6,2,0]
        #memo = {5: 1 + dfs(nums[5]), 6: 1 + dfs(nums[2]), 2: 1 + dfs(nums[0]), 0: 1 + dfs(nums[0])}

        memo = {}
        def dfs(index):
            if index in memo:
                return memo[index]
            if index in visited: # We found the beginning of the cycle
                memo[index] = 0

            else:
                visited.add(index)
                memo[index] = 1 + dfs(nums[index])
            return memo[index]
        for i in range(len(nums)):
            visited = set()
            dfs(i)
        return max(memo.values())