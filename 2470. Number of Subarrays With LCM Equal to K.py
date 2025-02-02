
"""
lcm(a,b) = (ab) / gcd(a,b)

lcm(a,b,c) = lcm(a,lcm(b,c))

lcm(3,6,2) = lcm(3,6) = 6

"""

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a,b):
    return a // gcd(a,b) * b

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        
        answer = 0
        n = len(nums)

        for i in range(n):
            l = nums[i]
            for j in range(i,n):
                l = lcm(l, nums[j])

                if l == k:
                    answer += 1
        return answer