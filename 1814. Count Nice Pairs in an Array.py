from math import comb
from collections import defaultdict
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        rev = lambda num: int(str(num)[::-1])
        diffs = defaultdict(list)
        #nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
        #nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
        # 2 numbers with same difference
        for num in nums:
            diffs[num - rev(num)] += [num]
        
        count = 0
        for diff in diffs:
            n = len(diffs[diff])
            count = (count + comb(n,2)) % (10**9 + 7)

        return count