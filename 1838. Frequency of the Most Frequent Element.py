"""
nums = [1,4,8,13], k = 5

Brute force solution would be O(n * k) (a nested for loop).

Sort the array, then use a sliding window method.

At the rth iteration:
    let l and r be the left and right boundary of the window.
    and let s = r - l + 1 the size of the window.

    we want the window to have a sum of s * nums[r].
    If that's not possible with k operations, shrink the window from the left.
    maximize the answer
"""

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        l = 0
        n = len(nums)
        currSum = 0
        answer = 0
        for r in range(n):
            size = r - l + 1
            requiredSum = size * nums[r]
            currSum += nums[r]

            while currSum + k < requiredSum:
                currSum -= nums[l]
                l += 1
                size = r - l + 1
                requiredSum = size * nums[r]
            
            answer = max(answer, r - l + 1)
        
        return answer
            