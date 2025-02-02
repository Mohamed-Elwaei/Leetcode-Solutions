class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        #AtLeast(k) = All subarrays - AtMost(k - 1)
        def AtMost(k, target):
            l = 0
            count = 0
            for r in range(len(nums)):
                if nums[r] == target:
                    k -= 1
                while k < 0:
                    if nums[l] == target:
                        k += 1
                    l += 1
                count += r - l + 1
            return count
        n = len(nums)
        return ((n * (n + 1)) // 2) - AtMost(k - 1, max(nums))