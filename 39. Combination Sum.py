class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = set()
        path = []
        sum = [0]
        def dfs():
            if sum[0] == target:
                combinations.add(tuple(sorted(path)))
            for c in candidates:
                if c + sum[0] <= target:
                    path.append(c)
                    sum[0] += c
                    dfs()
                    sum[0] -= c
                    path.pop()
        dfs()
        return combinations