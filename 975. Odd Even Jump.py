"""
During odd-numbered jumps (i.e., jumps 1, 3, 5, ...),
you jump to the index j such that arr[i] <= arr[j] and arr[j] is the smallest possible value. 

During even-numbered jumps (i.e., jumps 2, 4, 6, ...),
 you jump to the index j such that arr[i] >= arr[j] and arr[j] is the largest possible value.


We would use a binary search tree container.
We would use a sorted dictionary mapping each number to its index.

During odd-numbered jumps we find the first j>i such that arr[j] >= arr[i].
During even-numbered jumps we find the first j>i such that arr[j] <= arr[i].

"""


from sortedcontainers import SortedDict
class Solution:
    def oddEvenJumps(self, arr: list[int]) -> int:
        ans = 1
        n = len(arr)
        d = SortedDict({arr[-1]:n-1})

        possible = [[False,False] for _ in range(n)] #stores a tuple of 2 indicating if it is possible to reach the end using odd and even numbered jumps
        possible[-1] = [True,True]

        def bs(target,x): 
            # if x == 1 return index j of the smallest arr[j] >= target
            #id x == 0 return index j of the largest arr[j] <= target
            l,r = 0, len(d) - 1
            if x == 1:
                while l <= r:
                    mid = (r - l) // 2 + l

                    if d.peekitem(mid)[0] >= target:
                        r = mid - 1
                    else:
                        l = mid + 1
            else:
                while l <= r:
                    mid = (r - l) // 2 + l

                    if d.peekitem(mid)[0] <= target:
                        l = mid + 1
                    else:
                        r = mid - 1

            return d.peekitem(l)[1]
        
        for i in range(n-2,-1,-1):
            n = arr[i]

            j = bs(n,1)
            if arr[j] >= n:
                possible[i][0] = possible[j][1]
            
            j = bs(n,0)

            if arr[j] <= n:
                possible[i][1] = possible[j][0]
            
            if possible[i][0] or possible[i][1]:
                ans += 1
        return ans