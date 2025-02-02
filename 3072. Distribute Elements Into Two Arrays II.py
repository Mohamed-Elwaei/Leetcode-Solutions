"""
Easy to come up with a solution, but solution will be slow O(n^2).

How do we define an efficient greaterCount function?

We can use a sorted list for it.
"""

from sortedcontainers import SortedList

def greaterCount(arr, val):
    n = len(arr)
    index = arr.bisect_right(val)
    
    return n - index

class Solution:
    def resultArray(self, nums: list[int]) -> list[int]:
        A = SortedList([nums[0]])
        B = SortedList([nums[1]])

        arr1 = [nums[0]]
        arr2 = [nums[1]]
        
        n = len(nums)
        for i in range(2, n):
            res1 = greaterCount(A, nums[i])
            res2 = greaterCount(B, nums[i]) 
            if res1 > res2:
                A.add(nums[i])
                arr1.append(nums[i])
            elif res1 < res2:
                B.add(nums[i])
                arr2.append(nums[i])
            elif res1 == res2:
                if len(A) <= len(B):
                    A.add(nums[i])
                    arr1.append(nums[i])
                else:
                    B.add(nums[i])
                    arr2.append(nums[i])
        return arr1 + arr2