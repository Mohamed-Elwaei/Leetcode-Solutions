class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        path = []

        def dfs(i):
            if len(path) == k:
                combinations.append(path[:])
            for j in range(i,n+1):
                path.append(j)
                dfs(j+1)
                path.pop()
        dfs(1)
        return combinations