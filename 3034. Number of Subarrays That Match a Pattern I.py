from typing import List

def solve(nums: List[int], pattern: List[int]) -> int:
    # Translate pattern into comparison operations
    translated_pattern = []
    for p in pattern:
        if p == -1:
            translated_pattern.append(lambda x, y: x > y)
        elif p == 0:
            translated_pattern.append(lambda x, y: x == y)
        elif p == 1:
            translated_pattern.append(lambda x, y: x < y)
    
    m = len(pattern)
    n = len(nums)
    count = 0
    
    # Iterate over all subarrays of length m + 1
    for i in range(n - m):
        match = True
        for k in range(m):
            if not translated_pattern[k](nums[i + k], nums[i + k + 1]):
                match = False
                break
        if match:
            count += 1
            
    return count

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        return solve(nums, pattern)