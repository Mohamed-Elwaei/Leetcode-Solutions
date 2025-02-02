class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        inc = dec = 1
        last = nums[0]
        answer = 1
        for n in nums[1:]:
            if n > last:
                inc += 1
                dec = 1
            elif n < last:
                dec += 1
                inc = 1
            else:
                inc = dec = 1
            last = n
            answer = max(answer,inc,dec)
        return answer