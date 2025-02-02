"""
Brute force : O(2^n) Generate all subsets and see how many are beatiful.
"""

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n = len(nums)
        answer = 0
        for i in range(1, 1 << n):
            subset = set()
            valid = 1
            for j in range(n):
                if (i >> j) & 1:
                    if nums[j]-k in subset or nums[j]+k in subset:
                        valid = 0
                        break
                    subset.add(nums[j])
            answer += valid
        return answer