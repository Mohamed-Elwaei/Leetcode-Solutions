class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1,n+1)]
        paths = ['']
        k = [k]
        def dfs(path):
            if k[0]==0:
                return
            if len(path) == len(nums):
                k[0]-=1
                if not k[0]:
                    paths[0]=path
                return


            for i in nums:
                if k[0]==0:
                    return
                if i:
                    nums[i-1]=None
                    dfs(path+str(i))
                    nums[i-1] = i
        dfs('')
        return paths[0]
        
            
