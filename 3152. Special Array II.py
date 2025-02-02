"""
Brute force would be inefficient.
nums = [3,4,1,2,6], queries = [[0,4]]

arr = [1,0,1,0,0]

Store all bad pairs. Loop over the pairs for each query. If any pair is in [from, to] then the array nums[from .. to] is not special.

left to right = [0,0,0,0,1]

nums =          [3,4,1,2,6,1,4,5,7]
left to right = [0,0,0,0,1,1,1,1,2]

prefixsum[to] - prefixsum[from] should be 0 if the array is special.



"""


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        
        n = len(nums)
        prefix_sum = [0] * n

        for i in range(1,n):
            prefix_sum[i] = prefix_sum[i-1]
            if nums[i] & 1 == nums[i-1] & 1:
                prefix_sum[i] += 1
        

        #if there is a bad pair in nums[l .. r] then prefix_sum[r] will be more than prefix_sum[l]
        answer = []
        for l,r in queries:
            if prefix_sum[r] - prefix_sum[l] == 0:
                answer.append(True)
            else:
                answer.append(False)
        return answer
