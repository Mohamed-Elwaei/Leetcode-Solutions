class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        ans = set()

        def dfs(curr,index):

            if len(curr)>=2:
                ans.add(tuple(curr))
            
            for i in range(index,len(nums)):
                if nums[i]>=curr[-1]:
                    dfs(curr + [nums[i]],i + 1)
        
        for i in range(len(nums)):
            dfs([nums[i]],i+1)
        
        return ans

        