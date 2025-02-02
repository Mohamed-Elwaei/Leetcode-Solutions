class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        n = len(nums)
        answer = float('-inf')
        
        for i in range(1, 1 << n):
            strength = 1
            for j in range(0,32):
                if (i >> j) & 1:
                    strength *= nums[j]
            answer = max(answer, strength)
        return answer