M = int(1e9 + 7)

def maximumSubarraySum(arr):
    max_ = 0
    curr = 0
    for n in arr:
        curr = curr + n
        curr = max(curr, 0)
        max_ = max(max_, curr)
    return max_ 

class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        arr_sum = sum(arr)
        
        if k == 1:
            return maximumSubarraySum(arr) % M
        elif k == 2:
            return maximumSubarraySum(arr + arr) % M
        else:
            # Maximum subarray sum for arr + arr
            max_subarray_sum_twice = maximumSubarraySum(arr + arr)
            
            # If the sum of the array is positive, it can contribute further in k concatenations
            if arr_sum > 0:
                result = (max_subarray_sum_twice + (arr_sum * (k-2)) % M) % M
            else:
                result = max_subarray_sum_twice % M
            
            return result