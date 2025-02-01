class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        memo = dict()

        memo[(len(nums)-1),1] = memo[(len(nums)-1),-1] = 1

        def dfs(i,diff):
            if (i,diff) in memo:
                return memo[(i,diff)]
            longest = 0
            for j in range(i+1,len(nums)):
                if diff == 1:
                    if nums[j] < nums[i]:
                        longest = max(longest,dfs(j,-diff))
                elif diff == -1:
                    if nums[j] > nums[i]:
                        longest = max(longest, dfs(j,-diff))
            memo[(i,diff)] = 1 + longest 
                
            return memo[(i,diff)]
        return max(dfs(0,1),dfs(0,-1))
         