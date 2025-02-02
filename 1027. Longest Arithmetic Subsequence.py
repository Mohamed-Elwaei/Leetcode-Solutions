"""
This would be a DP problem.

let DP[i][j] be the longest sequence starting from index i with a difference of j.

for i in range [0,n] going backwards:
    
    for each k in range [i+1,n] going backwards:
        let diff = nums[k] - nums[i]
        DP[i][diff] = max(DP[i][diff], 1 + DP[k][diff])

answer = max cell in DP
"""

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        memo = {} #Map each (index, diff) to the longest arithmetic subsequence starting at index with difference diff.
        n = len(nums)
        for i in range(n-1,-1,-1):

            for j in range(i+1, n):
                diff = nums[j] - nums[i]
                memo[(i, diff)] = memo.get((i, diff), 1)

                if (j, diff) in memo:
                    memo[(i, diff)] = max(memo[(i, diff)], memo[(j, diff)] + 1)
                else:
                    memo[(i, diff)] = max(memo[(i, diff)], 2)
        
        return max(memo.values())