def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)


"""

[3,9,27,81,99]

"""




class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        

        answer = 0
        n = len(nums)
        for i in range(n):
            g = nums[i]
            for j in range(i,n):
                g = gcd(g,nums[j])

                if g == k:
                    answer += 1
        return answer