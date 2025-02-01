"""

nums = [1,1,1], k = 2
nums[0:1] and nums[1:2]

nums = [1,2,3], k = 3
nums[0:1] and nums[2:2]



nums = [1,1,1], k = 2
nums = [1,2,3]

for each nums[i]: let's consider all subarrays ending at nums[i].

If we know that the sum(nums[0...i]) = x, we want to find a sum(nums[0...j]) = y such that j <= i
and x - y = k.
And we want to know how many different j's there are.


Solution:
Use a Hash map.
Each key k will map to an integer y such that there are y subarrays starting from the beggining with a sum of k.

At each nums[i] we calculate the sum(nums[0...i]) = x and we figure out how many y's we have.
"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        D = {0:1}

        answer = 0
        x = 0

        for n in nums:
            x += n
            #We have x, how many subarrays with sum y starting from the beginning satisfy x - y = k.

            if x - k in D:
                answer += D[x - k]
            
            D[x] = D.get(x,0) + 1
        return answer


        