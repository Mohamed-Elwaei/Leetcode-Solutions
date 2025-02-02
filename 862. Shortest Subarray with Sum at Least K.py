"""
One other idea would be do a binary search from [1, len(nums)]
That wouldn't work because if we had nums = [1,-1,-1,-1] and k = 1
Then we wouldn't have a monotonic structure.

For each nums[i], calculate the shortest subarray with sum k that ends with nums[i].

k is positive, if the subarray is negative, then we can start over.

We can use a sliding window approach.
If the sum of the window is more than or equal to k, we can decide if we can shrink the window from the left.

We can shrink the window from the left if sum(window) - window[left]  >= min(k, sum(window))


nums = [-1,-1,1,-1,-1] k = 1

"""
class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        def F(nums):
            l = 0
            n = len(nums)
            sum_ = 0
            answer = float('inf')
            for r in range(n):
                sum_ += nums[r]
                while sum_ - nums[l] >= min(k, sum_) and l < r:
                    sum_ -= nums[l]
                    l += 1
                
                if sum_ >= k:
                    answer = min(r - l + 1, answer)
            
            
            return answer
        
        ans = min(F(nums[:-1]), F(nums))

        if ans == float('inf'):
            return -1
        return ans
        


s = Solution()
print(s.shortestSubarray([84,-37,32,40,95], 167))