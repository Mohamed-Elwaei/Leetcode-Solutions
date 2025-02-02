"""
if destination = [x,y]

then there are (x + y)Cx or (x + y)Cy possible paths.

We can generate all (x + y)Cx paths and sort them and pick the kth path.

destination = [2,3], k = 1

[
    "HHHVV", (3,4), (0,1,2)
    "HHVHV", (2,4), (0,1,3)
    "HHVVH", (2,3)  (0,1,4)
    "HVHHV", (1,4)  (0,2,3)
    "HVHVH", (1,3)  (0,2,4)
    "HVVHH", (1,2)  (0,3,4)
    "VHHHV", (0,4)  (1,2,3)
    "VHHVH", (0,3)  (1,2,4)
    "VHVHH", (0,2)  (1,3,4)
    "VVHHH"  (0,1)  (2,3,4)
]
At the beginning we have [1, 5C3] or [1, 10] paths to consider

So if we decide there will be an H at 0.

We will have 2 more H's and 4 more positions.
That leaves with 4C2 = 6 combinations which have an H at 0.
Now we have [1, 6] paths to consider.

If we decide to have an H at 1 after placing an H at 0, then we will have 1 more H to consider and 3 more positions.
THat leaves with 3C1 combinations with an H at 0 and 1.
Now we have [1, 3] paths to consider. The first 3 paths have an H at index 0 and 1.


"""
from math import comb

class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        h_count = destination[1]


        h_positions = []
        length = sum(destination)

        def F(start, left, right, h_count):
            if k < left or k > right:  
                return False
            if left == k and right == k:
                return True
            left_boundary = left
            for i in range(start, length):
                h_positions.append(i)
                leftover_positions = (length - (i + 1))
                leftover_h = h_count - 1
                tmp = comb(leftover_positions, leftover_h)

                if F(i + 1, left_boundary, left_boundary + tmp - 1, leftover_h):
                    return True
                h_positions.pop()
                left_boundary = left_boundary + tmp
            return False

        F(0, 1, comb(length, h_count), h_count)

        ret = ''
        last = h_positions[-1] + 1
        while len(h_positions) < h_count:
            h_positions.append(last)
            last += 1
        h_positions = set(h_positions)

        for i in range(length):
            if i in h_positions:
                ret += 'H'
            else:
                ret += 'V'
        return ret