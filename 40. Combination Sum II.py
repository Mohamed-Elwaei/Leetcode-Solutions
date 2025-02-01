class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(i):
            if sum[0] == target:
                paths.append(path[:])
            if i >= len(candidates): return
            
            for j in range(i,len(candidates)):
                if j>i and candidates[j] == candidates[j-1]:
                    continue
                if sum[0] + candidates[j] <= target:
                    path.append(candidates[j])
                    sum[0] += candidates[j]
                    dfs(j + 1)
                    sum[0] -= candidates[j]
                    path.pop()
        paths = []
        path = []
        candidates.sort()
        sum = [0]
        dfs(0)
        return paths