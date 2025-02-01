class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(i):
            if len(path) == k:
                if sum[0] == n:   paths.append(path[:])
                return
            for j in range(i, 10):
                if sum[0] + j <= n:
                    sum[0] += j
                    path.append(j)
                    dfs(j + 1)
                    sum[0] -= j
                    path.pop()
        paths = []
        path = []
        sum = [0]
        dfs(1)
        return paths