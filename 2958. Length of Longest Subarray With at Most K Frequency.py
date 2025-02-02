
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counter = {i:0 for i in nums}
        N = len(nums)
        l = 0
        answer = 0
        for r in range(N):
            
            counter[nums[r]] += 1
            
            while counter[nums[r]] > k:
                counter[nums[l]] -= 1
                l += 1
            answer = max(answer, r - l + 1)
        return answer