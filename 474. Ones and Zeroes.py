class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        #State parameters: m = zeroes, n = ones, visited 
        #return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.
        #We don't want to pick the same index or string twice.
        #Greedy approach does not work.

        counter = [(s.count('0'),s.count('1'),s) for s in strs]
        memo = {}
        def dfs(m,n,i):
            if i >= len(strs):
                return 0
            if (m,n,i) in memo:
                return memo[(m,n,i)]
            else:
                zeroes,ones,_ = counter[i]
                if m - zeroes >= 0 and n - ones >= 0:
                    memo[(m,n,i)] = max(1 + dfs(m - zeroes,n - ones, i+1), dfs(m,n, i + 1))
                else: memo[(m,n,i)] = dfs(m,n, i + 1)
                return memo[(m,n,i)]
        return dfs(m,n,0)