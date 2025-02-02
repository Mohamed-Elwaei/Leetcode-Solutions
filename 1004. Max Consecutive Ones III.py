class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        #[1,1,1,0,0,0,1,1,1,1,0] => {0:-1, 1:3, 2:4, 3:5, 4:10}
        prefixSum = {0: -1}
        flips = 0
        longest = 0
        for i,n in enumerate(nums):
            flips += n == 0
            if flips not in prefixSum:
                prefixSum[flips] = i
            longest = max(longest, i - prefixSum[max(flips - k,0)])
        return longest
        