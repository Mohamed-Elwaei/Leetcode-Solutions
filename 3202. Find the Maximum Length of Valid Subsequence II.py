"""
a mod k = c
b mod k = d

(a + b) mod k = (c + d) mod k.




k iteration from [0,k-1].


Each iteration we calculate F(nums, k, i).

F(nums, k, i) calculate the longest valid subsequence with (sub[0] + sub[1]) % k == i.



nums = [1,4,2,3,1,4], k = 3

i = 0 longest subsequence [1,2,1].
i = 1 longest subsequence [1,3,1] or [4,3,4].
i = 2 longest subsequence [1,4,1,4]
"""


def F(nums,k,i):
    
    #classes[i] longest subsequence ending with nums[j] where 0 <= j < len(nums) and nums[j] % k = i.
    classes = [0] * k
    
    #If we have a mod k == c and we know that (c + d) mod k == i. We look for classes[c] and put classes[c] + 1 in classes[d].
    
    for n in nums:
        x = n % k
        y = (k - x + i) % k
        
        classes[x] = classes[y] + 1
    
    return max(classes)

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(k):
            ans = max(ans, F(nums, k, i))
        return ans