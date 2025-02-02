"""
If nums[i] == nums[k+i] for some integers i and k, then we have to include both.


So count how many good subarrays we have.
Find out how many ways we can merge them.

Then the problem simplifies to:

let n = number of intervals we have.


for k in range([0,n-1]):
    answer += nCk.

answer will be 2^(n-1) in closed form.

1st example.
nums = [1,2,3,4]

good subarrays are [1], [2], [3], [4]

n = 4

2^(4-1) = 8

nums = [1,1,1,1]
good subarrays are [1,1,1,1]

answer = 2^(1-1) = 1


3rd example

nums = [1,2,1,3]

good subarrays are [1,2,1], [3]
a
answer = 2^(2-1) = 2

"""

def pow(a,b,m):

    if b == 0:
        return 1
    
    u = pow(a,b//2,m)

    res =(u * u) % m

    if b & 1:
        res = (res * a) % m
    return res 




class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        last = dict() # maps each number to its first occurrence
        m = int(1e9 + 7)
        for index,number in enumerate(nums):
            last[number] = index

        
        subarrays = 1 #good subarrays we have.
        end = last[nums[0]]

        for i in range(len(nums)):
            if i > end:
                subarrays += 1
            
            end = max(end,last[nums[i]])

        return pow(2, subarrays - 1, m)