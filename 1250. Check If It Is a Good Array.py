"""
let n = size of the array 
let k = maximum number in nums.


Time Complexity: O(n*log(k))
Memory Complexity: O(log(k))

"""
def gcd(a,b):
    while b != 0:
        a,b = b, a%b
    return a

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        n = len(nums)

        g = gcd(nums[0],nums[0])

        for i in range(n):
            g = gcd(nums[i],g)
        return g == 1