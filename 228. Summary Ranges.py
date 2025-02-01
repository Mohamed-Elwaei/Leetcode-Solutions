class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        l,r = 0,0

        ans = []

        for n in nums:
            if len(ans) == 0 or ans[-1][-1]!=n-1:
                ans.append([n,n])
            else:
                ans[-1][-1] = n
        
        for i in range(len(ans)):
            if ans[i][0] == ans[i][1]:
                ans[i] = f'{ans[i][0]}'
            else:
                ans[i] = f'{ans[i][0]}->{ans[i][1]}'
        return ans

        