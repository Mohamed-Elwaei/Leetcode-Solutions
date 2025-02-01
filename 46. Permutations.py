class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res=[]
        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr)
            
            for n in nums:
                if  n not in curr:
                    dfs(curr + [n]) 
        

        for n in nums:
            dfs([n])
        return res
        