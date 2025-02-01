class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # [23,2,4,6,7] => [23,25,29,35,42]
        #                  Subtract index of 29 from index of 23 = 2 - 0
        # [23,2,6,4,7] => [23,25,31,35,42]
        #                  Subtract index of 42 from -1 which is the default so 4 - (-1) = 5
        # Modular arithmetic: a % k = n and b % k = n, then (a - c) % k = (b - c)  % k
        #Time complexity is O(N) where N is the size of our nums array
        for i in range(1,len(nums)):
            nums[i] += nums[i - 1]

        prefixSum = {0:-1}
        #Memory complexity is O(k).
        for i in range(len(nums)):
            if nums[i] % k not in prefixSum:
                prefixSum[nums[i] % k] = i
            else:
                if i - prefixSum[nums[i] % k] >= 2:
                    return True
        return False